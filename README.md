# VectorFlow

VectorFlow is a Streamlit-based application designed to help users interactively explore and analyze their documents using advanced natural language processing techniques.

## Overview

VectorFlow allows users to upload PDF documents, process them, and then ask questions about the content of those documents. It employs various NLP models and techniques to extract text from PDFs, split the text into meaningful chunks, generate embeddings for those chunks, and enable conversational interactions based on the processed data.

## Features

- **PDF Processing**: Users can upload one or multiple PDF documents, which will be processed to extract text.
  
- **Text Chunking**: The extracted text is segmented into smaller, meaningful chunks to facilitate more efficient analysis.

- **Embedding Generation**: Text chunks are embedded into numerical vectors using state-of-the-art embedding models like OpenAI Embeddings and Hugging Face Instruct Embeddings.

- **Conversational Interface**: Users can ask questions about the uploaded documents using a conversational interface, powered by ChatOpenAI model and a conversation chain.

## Setup

To run VectorFlow locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/marlin-spike/VectorFlow
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   
   - Obtain an OpenAI API key and set it as an environment variable:
   
     ```
     export OPENAI_API_KEY="your-openai-api-key"
     ```

4. Run the application:

   ```
   streamlit run app.py
   ```

## Usage

Upon running the application, you'll be presented with a user interface where you can:

- Upload PDF documents.
- Click on the "Process" button to extract text from the uploaded PDFs and generate embeddings.
- Ask questions about the uploaded documents in the text input field provided.

## Contributing

Contributions are welcome! If you'd like to contribute to VectorFlow, please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

## Credits

VectorFlow was created by [Your Name] and is maintained by [Your Organization]. It utilizes various open-source libraries and models, including Streamlit, PyPDF2, OpenAI, Hugging Face, and others.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.