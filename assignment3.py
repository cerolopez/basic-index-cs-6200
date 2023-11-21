from elasticsearch import Elasticsearch, helpers
import parse_functions
import os
from dotenv import load_dotenv
load_dotenv()

es_url = os.getenv("ELASTICSEARCH_URL")
es_api = os.getenv("ELASTICSEARCH_API")
index_name = os.getenv("INDEX_NAME")
tags = ["docno", "head", "byline", "dateline", "text"]

# specify relative path
relative_path = "AP_DATA/ap89_collection"
folder_path = os.path.join(os.getcwd(), relative_path)

print("folder path", folder_path)

documents = parse_functions.parse_documents(folder_path, index_name, tags)

def batch_docs(documents, batch_size=1000, index_name="search-assignment-3-final"):
    es = Elasticsearch(es_url,
  api_key=es_api, 
  timeout=30, 
  max_retries=5
)
    
    doc_batches = [documents[i:i + batch_size] for i in range(0, len(documents), batch_size)]

    for batch in doc_batches:
        actions = [
            {
                "_op_type": "index", 
                "_index": index_name,
                "_source": document
            }
            for document in batch
        ]

        success, failed = helpers.bulk(es, actions)
        print(f"Indexed {success} docs. Failed to index {failed} docs.")

batch_docs(documents)