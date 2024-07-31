import os
import logging
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import openai

# Configure logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

openai.api_type = "azure"
openai.api_base = os.environ["AZURE_OPENAI_ENDPOINT"]
openai.api_version = os.environ["AZURE_OPENAI_API_VERSION"]
openai.api_key = os.environ["AZURE_OPENAI_API_KEY"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    logging.debug('Summarize endpoint called')
    if 'file' not in request.files:
        logging.error('No file part in the request')
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        logging.error('No selected file')
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        logging.debug(f'File saved to {filepath}')

        # Read PDF content
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        logging.debug(f'Extracted text: {text[:500]}...')  # Log only the first 500 characters

        # Summarize using OpenAI model
        prompt = f"You are an assistant that summarizes documents. Summarize the following content in a concise manner:\n\n{text}"
        try:
            logging.debug(f'Prompt: {prompt}')
            response = openai.Completion.create(
                engine="gpt-35-turbo",  # Use your actual deployment name
                prompt=prompt,
                max_tokens=150
            )
            logging.debug(f'Response: {response}')
            summary = response.choices[0].text.strip()
            logging.debug(f'Summary: {summary}')
            return jsonify({'summary': summary})
        except openai.error.InvalidRequestError as e:
            logging.error(f'Error from OpenAI: {e}')
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
