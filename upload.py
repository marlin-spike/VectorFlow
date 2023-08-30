from flask import Flask, request, jsonify
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
import tempfile
from docx2txt import process
import os

app = Flask(__name__)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)

def load_and_process_text(file):
    # Check if the file is a PDF
    if file.filename.lower().endswith('.pdf'):
        with file.stream as pdf_stream:
            pdf_data = pdf_stream.read()
            texts = text_splitter.split_documents(pdf_data)
            return texts
    # If not a PDF, assume docx or txt
    elif file.filename.lower().endswith(('.docx', '.txt')):
        with file.stream as text_stream:
            text_data = text_stream.read().decode('utf-8')
            texts = text_splitter.split_documents(text_data.encode('utf-8'))
            return texts
    else:
        return None

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    texts = load_and_process_text(file)

    if texts is None:
        return jsonify({'error': 'Unsupported file format'})

    return jsonify({'texts': texts})

if __name__ == '__main__':
    app.run(debug=True)
#run