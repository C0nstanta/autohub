import os
os.environ["OPENAI_API_KEY"] = "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"

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader(input_dir="data").load_data()
index = VectorStoreIndex.from_documents(documents)
index.storage_context.persist(persist_dir="index")

print("✅ Index created and saved in ./index")
