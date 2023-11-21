# ElasticSearch index on Flask
This is a basic implementation of an ElasticSearch index on a simple Flask web app, using documents from AP. This code includes functions that parses data so that it can be ingested into ElasticSearch in batches of 1000, but it can also be used with an existing Elasticsearch index. To use, follow these steps:

Download the repo and run this command in Terminal to install dependencies:
pip install -r requirements.txt

Download the dataset labeled AP_DATA and add to root directory (link coming soon).

Update the .env with your own Elasticsearch URL, API key, and index name.

If you want to use different dataset and parse/ingest to an existing ElasticSearch index, you'll need to update the relative path in the file labeled assignment3.py. You'll also need to update the specified tags. The file search-results.html should be updated with the new tags as well.
