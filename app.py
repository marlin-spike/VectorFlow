from flask import Flask, request, jsonify
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
import os
import tempfile
from docx2txt import process

app = Flask(__name__)

# Set the directory to store temporary files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize text splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)

def convert_to_pdf(file_path, temp_dir):
    # Convert non-PDF files to PDF using appropriate methods
    if file_path.lower().endswith('.docx'):
        text = process(file_path)
        pdf_path = os.path.join(temp_dir, 'converted.pdf')
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(PdfReader(text.encode('utf-8')).to_pdf())
        return pdf_path
    elif file_path.lower().endswith('.txt'):
        # Perform similar conversion for text files
        pass
    return None

@app.route('/upload', methods=['POST'])
def upload_and_process_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        temp_dir = tempfile.mkdtemp(dir=app.config['UPLOAD_FOLDER'])
        temp_file_path = os.path.join(temp_dir, file.filename)
        file.save(temp_file_path)

        if not temp_file_path.lower().endswith('.pdf'):
            pdf_path = convert_to_pdf(temp_file_path, temp_dir)
            if pdf_path:
                temp_file_path = pdf_path
            else:
                return jsonify({'error': 'Unsupported file format'})

        with open(temp_file_path, 'rb') as pdf_file:
            data = pdf_file.read()
            texts = text_splitter.split_documents(data)
            # Process the 'texts' as needed

        os.remove(temp_file_path)
        os.rmdir(temp_dir)

        return jsonify({'message': 'File uploaded and processed'})

if __name__ == '__main__':
    app.run(debug=True)
#run