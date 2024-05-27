import os
from os.path import join, dirname
from dotenv import load_dotenv
from VectorDB import createVectorDB
from langchain_community.vectorstores.utils import filter_complex_metadata

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
URLS = ["https://towardsdatascience.com/text-classification-sentiment-analysis-on-r-sgexams-4ea341134fba"]
FIRECRAWL_API_KEY = os.environ.get("FIRECRAWL_API_KEY")

def main():
    retriever = createVectorDB(URLS, 250, 0, FIRECRAWL_API_KEY)  
    print(retriever, type(retriever))
    
if __name__ == "__main__":
    main()