## PDF Summarizer with Retrieval-Augmented Generation (RAG)
This project is a web application that leverages the power of Retrieval-Augmented Generation (RAG) to create a sophisticated PDF summarizer. Users can upload PDF files, and the application extracts and summarizes the content using OpenAI's GPT-35-turbo model.

## Features

  ->  **PDF File Upload:** Supports PDF file uploads for summarization.

  ->  **Text Extraction:** Efficiently extracts text from uploaded PDF documents.
  
  ->  **Summarization:** Utilizes OpenAI's GPT-35-turbo model to generate accurate and concise summaries.
  
  ->  **User-friendly Interface:** Displays summaries in a clean and easy-to-use interface.
  
  ->  **Context Preservation:** Maintains the context of the document to provide coherent and relevant summaries.


## Technologies Used
  
  ->  **Python:** The core programming language used for the backend logic.
  
  ->  **Flask:** A lightweight WSGI web application framework for the backend.
  
  ->  **OpenAI GPT-35-turbo:** For generating intelligent summaries.
  
  ->  **FAISS:** For efficient similarity search and clustering of dense vectors.
  
  ->  **LangChain:** For creating the chain of retrieval and generation tasks.
  
  ->  **dotenv:** For managing environment variables.
  
  ->  **Conda:** For managing the project's environment and dependencies.

## Results

![image](https://github.com/user-attachments/assets/44792dc0-198f-4b4e-89cb-5f2c449979b8)
![image](https://github.com/user-attachments/assets/cfc602a0-5ee6-48c9-8505-bb69cac0710d)


## Retrieval-Augmented Generation (RAG)
This project utilizes the concept of Retrieval-Augmented Generation (RAG) to enhance the accuracy and relevance of the generated summaries. RAG combines the power of retrieval (finding relevant documents) and generation (creating summaries) to provide more informed and context-aware summaries. The workflow is as follows:

  ->  **Document Loading:** The uploaded PDF document is parsed and split into manageable chunks.
  ->  **Embedding Generation:** Each chunk is converted into dense vectors using Azure OpenAI Embeddings.
  ->  **Retrieval:** Relevant chunks are retrieved based on their similarity to the input query.  
  ->  **Summary Generation:** The retrieved chunks are fed into the GPT-35-turbo model to generate accurate and contextually relevant summaries.

## Installation

**Prerequisites**

Python 3.9 or above
Conda

**Setup**
**Clone the repository:**
git clone <repository_url>
cd pdf_summarizer

**Create and activate a Conda environment:**
conda create --name pdf_summarizer python=3.9
conda activate pdf_summarizer

**Install the required dependencies:**
pip install -r requirements.txt

**Set up environment variables:**

Create a .env file in the root directory and add your Azure OpenAI endpoint and API key:
AZURE_OPENAI_ENDPOINT=https://<your-endpoint>.openai.azure.com/
AZURE_OPENAI_API_KEY=<your-api-key>
AZURE_OPENAI_API_VERSION=2024-02-15-preview

## Usage
**Run the Flask application:**
python app.py

**Open your browser and go to:**
http://127.0.0.1:5000/

**Upload a PDF file:**

Click on the "Choose file" button and select a PDF file from your computer. The application will process the file, extract text, and generate a summary which will be displayed on the interface.

## Project Structure

pdf_summarizer/

├── app.py

├── requirements.txt

├── templates/

│   └── index.html

├── uploads/

└── .env

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
