import os
from os.path import join, dirname
from dotenv import load_dotenv
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_community.chat_models import ChatOllama
from VectorDB import createVectorDB
from RetrievalGrader import retrievalGrader
from AnswerGen import generateResponse
from WebSearch import tavilySearchTool
from HallucinationGrader import hallucinationGrader

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
URLS = ["https://towardsdatascience.com/text-classification-sentiment-analysis-on-r-sgexams-4ea341134fba"]
FIRECRAWL_API_KEY = os.environ.get("FIRECRAWL_API_KEY")
TAVILLY_API_KEY = os.environ.get("TAVILY_API_KEY")

GRADER_LLM = ChatOllama(model="llama3", format="json", temperature=0)
GEN_LLM = ChatOllama(model="llama3", temperature=0)

def main():
    retriever = createVectorDB(URLS, 250, 0, FIRECRAWL_API_KEY)  
    # output = retrievalGrader(retriever=retriever, llm=GRADER_LLM, question="What is sentiment analysis of Secondary school?")
    # print(output)

    output, docs = generateResponse(retriever=retriever, llm=GEN_LLM, question="What is sentiment analysis of Secondary school?")
    print(output)

    output = hallucinationGrader(output, docs)
    print(output)

if __name__ == "__main__":
    main()