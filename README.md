# HEAP-AI-Workshop

# 1st half of workshop [OpenAI API Integration to Frontend] [WIP]

## Frontend directory
Make sure you have nodejs `v20.10.0` or higher and npm `10.2.3` or higher installed. Install dependencies with:
```
npm install
```
Once it's done start up a local server with:
```
npm run dev
```
To create a production build:
```
npm run build
```

# 2nd half of workshop [Building reliable Retrieval Augmented Generation(RAG) AI Architecture]
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
