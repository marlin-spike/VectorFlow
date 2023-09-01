# VectorFlow: Supercharging Your PDFs

Welcome to **VectorFlow**, a cutting-edge Flask and React application that transforms your PDF documents into intelligent resources. With VectorFlow, your PDFs become more than just files – they're your source of quick, accurate insights.

## Features

- **PDF Intelligence**: Upload any PDF document, and VectorFlow works its magic.
- **Chunkification**: LongChain technology breaks your PDF into smart, manageable chunks.
- **AI Vectorization**: OpenAI's power converts these chunks into smart vectors.
- **Data Storage**: Pinecone Vector Database stores your vectors for instant access.
- **Question & Answer**: Ask questions, and VectorFlow finds answers using cosine similarity.
- **React UI**: Enjoy a user-friendly interface built with React.

## Get Started

<!-- 1. Clone the repository.
2. Install dependencies with `npm install` and `pip install`.
3. Run the app with `npm start` and `python app.py`.-->







### Set up your API keys and endpoints in the `secret` folder

1.  Create a new file `secret/openai_api_key` and paste your [OpenAI API key](https://platform.openai.com/docs/api-reference/authentication) into it:

`echo "your_openai_api_key_here" > secret/openai_api_key`

2.  Create a new file `secret/pinecone_api_key` and paste your [Pinecone API key](https://docs.pinecone.io/docs/quickstart#2-get-and-verify-your-pinecone-api-key) into it:

`echo "your_pinecone_api_key_here" > secret/pinecone_api_key`

When setting up your pinecone index, use a vector size of `1536` and keep all the default settings the same.

3.  Create a new file `secret/pinecone_api_endpoint` and paste your [Pinecone API endpoint](https://app.pinecone.io/organizations/) into it:

`echo "https://example-50709b5.svc.asia-southeast1-gcp.pinecone.io" > secret/pinecone_api_endpoint`



## Usage

1. Upload a PDF.
2. Watch as VectorFlow transforms it into smart chunks.
3. Ask questions to get insightful answers.

## Project Name: VectorFlow

Your PDFs, supercharged with VectorFlow. Dive in now !!!

