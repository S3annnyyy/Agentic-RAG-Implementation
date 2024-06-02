import langchain_community.chat_models.ollama as llmType
import langchain_core.vectorstores as rtrType
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate 


LLM = ChatOllama(model="llama3", format="json", temperature=0)

RETRIEVAL_PROMPT = PromptTemplate(
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

GRADING_PROMPT = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a grader assessing 
    whether an answer is useful to resolve a question. Give a binary score 'yes' or 'no' to indicate 
    whether the answer is useful to resolve a question. Provide the binary score as a JSON with a 
    single key 'score' and no preamble or explanation. <|eot_id|><|start_header_id|>user<|end_header_id|> 
    Here is the answer: {generation}
    -----
    Here is the question: {question} <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
    input_variables=["generation", "question"],
)

HALLUCINATION_PROMPT = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a grader assessing
    whether an answer is grounded in / supported by a set of facts. Give a binary score 'yes' or 'no' to
    indicate whether the answer is grounded in / supported by a set of facts.
    Provide the binary score as a JSON with a single key 'score' and no preamble or explanation.
    <|eot_id|><|start_header_id|>user<|end_header_id|> Here are the facts:
    {documents}
    -----
    Here is the answer: {generation} <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
    input_variables=["generation", "documents"],
)

def hallucinationGrader(answerGenerated, docs):
    """
    """
    hGrader = HALLUCINATION_PROMPT | LLM | JsonOutputParser()
    outcome = hGrader.invoke({"documents": docs, "generation": answerGenerated}) 
    return outcome

def retrievalGrader(retriever: rtrType.VectorStoreRetriever, question: str):
    """
    """
    grader = RETRIEVAL_PROMPT | LLM | JsonOutputParser()

    docs = retriever.invoke(question)

    doc_txt = docs[1].page_content

    output_grade = grader.invoke({"question": question, "document": doc_txt})

    return output_grade

def answerGrader(answerGenerated, docs):
    """
    """
    aGrader = GRADING_PROMPT | LLM | JsonOutputParser()
    outcome = aGrader.invoke({"question": docs, "generation": answerGenerated}) 
    return outcome