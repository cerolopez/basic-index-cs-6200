from flask import Flask, request, render_template
from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv
load_dotenv()

es_url = os.getenv("ELASTICSEARCH_URL")
es_api = os.getenv("ELASTICSEARCH_API")
index_name = os.getenv("INDEX_NAME")

print("URL: ", es_url)
print("API: ", es_api)

es = Elasticsearch(es_url,
  api_key=es_api
)
print("Connected to ElasticSearch cluster")

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Home"

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        query = request.form["query"]
        results = perform_elasticsearch(query)
        print("length: ", len(results))
        return render_template("search_results.html", results=results, query=query)
    return render_template("index.html")

def perform_elasticsearch(query):
    try:
        result = es.search(index='search-assignment-3-final', body={'query': {'match': {'text': query}}}, size=10)

        return result["hits"]["hits"]
    except Exception as e:
        print(f"Elasticsearch search error: {e}")
        return []

if __name__ == "__main__":
    app.run(debug=True)