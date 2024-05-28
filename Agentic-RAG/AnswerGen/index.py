import langchain_community.chat_models.ollama as llmType
import langchain_core.vectorstores as rtrType 
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

ANSGEN_PROMPT = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are an assistant for question-answering tasks.
    Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know.
    Use three sentences maximum and keep the answer concise <|eot_id|><|start_header_id|>user<|end_header_id|>
    Question: {question}
    Context: {context}
    Answer: <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
    input_variables=["question", "document"],
)

def generateResponse(retriever: rtrType.VectorStoreRetriever, llm: llmType.ChatOllama, question: str):
    """
    """
    rag_chain = ANSGEN_PROMPT | llm | StrOutputParser()
    docs = retriever.invoke(question)
    response = rag_chain.invoke({"context": docs, "question": question})
    return response, docs 