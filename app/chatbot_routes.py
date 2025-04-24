from flask import Blueprint, request, jsonify
import os
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage

# Load API key (can also be done in __init__.py globally)
os.environ["OPENAI_API_KEY"] = "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"  # Replace securely

# Load index once
storage_context = StorageContext.from_defaults(persist_dir="index")
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()

chatbot = Blueprint('chatbot', __name__)

@chatbot.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    if not question:
        return jsonify({'error': 'No question provided'}), 400

    response = query_engine.query(question)
    return jsonify({'answer': str(response)})
