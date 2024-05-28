import langchain_community.chat_models.ollama as llmType
import langchain_core.vectorstores as rtrType 
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate

GRADER_PROMPT = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>You are a grader assessing relevance
    of a retrieved document to a user question. If the document contains keywords related to the user question,
    grade it as relevant. It does not need to be a stringent test. The goal is to filter out erroneous retrievals. \n
    Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question. \n
    Provide the binary score as a JSON with a single key 'score' and no preamble or explanation. 
    <|eot_id|><|start_header_id|>user<|end_header_id|>
    Here is the retrieved document: \n\n{document} \n\n
    Here is the user question: {question} \n <|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """,
    input_variables=["question", "document"]
)

def retrievalGrader(retriever: rtrType.VectorStoreRetriever, llm: llmType.ChatOllama, question: str):
    """
    """
    grader = GRADER_PROMPT | llm | JsonOutputParser()

    docs = retriever.invoke(question)

    doc_txt = docs[1].page_content

    output_grade = grader.invoke({"question": question, "document": doc_txt})

    return output_grade