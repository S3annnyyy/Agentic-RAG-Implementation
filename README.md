# Agentic RAG Implementation

## Building reliable Retrieval Augmented Generation(RAG) AI Architecture
![image](https://github.com/S3annnyyy/HEAP-AI-Workshop/assets/67400060/0d500237-f8a7-45dd-a04c-5390c5b1b795)

Make sure you have Python `3.10.9` or higher and pip `24.0` or higher installed. Install dependencies with:
```
pip install requirements.txt
```
Configuring environment.
1. Create free-tier accounts from [Firecrawl](https://www.firecrawl.dev/) &  [Tavily AI](https://tavily.com/)
2. Create `.env` under `Agentic-RAG folder` and populate folder in this manner:
```
FIRECRAWL_API_KEY=XXX
TAVILY_API_KEY=XXX
```
3. Download [ollama](https://www.ollama.com/) and download llama3 model by running the following in command prompt:
```
ollama run llama3
~Should take about 30mins unless your laptop trash af 
```  
Once it's done start up by running this command in the terminal:
```
python main.py
```
