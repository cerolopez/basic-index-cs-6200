from bs4 import BeautifulSoup
import os

def parse_document(file_path, index_name, tags, documents):
    
    html_content = ""
    
    with open(file_path, "r", encoding="utf-8", errors="replace") as file:
        html_content = file.read()
        
    parsed_doc = BeautifulSoup(html_content, 'html.parser')
    
    all_docs = parsed_doc.find_all("doc")
    
    for doc_tag in all_docs:
        index_content = {}
        
        for child in doc_tag.children:
            if child.name in tags:
                index_content[child.name] = child.text
                
        documents.append(index_content)
        
    return documents

def parse_documents(folder_path, index_name, tags):
    documents = []
    
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return
        
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        parse_document(file_path, index_name, tags, documents)
        
    return documents