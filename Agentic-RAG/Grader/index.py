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

# CONDITIONAL EDGE
def hallucinationGrader(state: dict):
    """
    """
    question = state["question"]
    documents = state["documents"]
    generation = state["generation"]
    hallucinationGrader = HALLUCINATION_PROMPT | LLM | JsonOutputParser()
    answerGrader = GRADING_PROMPT | LLM | JsonOutputParser()

    hallucination_score = hallucinationGrader.invoke({"documents": documents, "generation": generation})
    hallucination_grade = hallucination_score["score"]

    if hallucination_grade.lower() == "yes":
        print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS") 
        print("---GRADE GENERATION vs QUESTION---")
        answer_score = answerGrader.invoke({"question": question, "generation": generation})
        answer_grade = answer_score["score"]

        if answer_grade.lower() == "yes":
            print("---DECISION: GENERATION ANSWERS QUESTION, NOT HALLUCINATION")
            return "useful"
        else:
            print("---DECISION: GENERATION IS A HALLUCINATION")
            return "not useful"
    else:
        print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS")
        return "not supported"


def retrievalGrader(state: dict):
    """
    This function determins if any retrieved documents are relevant to the question.
    If not relevant => Set flag to run web search

    Args:
        state: The current graph state
    
    Returns:
        state: Filtered to contain only relevant documents + updated web search state 
    """
    # Init retrieval grader
    retrieval_grader = RETRIEVAL_PROMPT | LLM | JsonOutputParser()

    print("---CHECK DOCUMENT RELEVANCE TO THE QUESTION---")
    question = state["question"]
    documents = state["documents"]

    filtered_docs = []
    web_search = "No"
    for doc in documents:
        score = retrieval_grader.invoke({"question": question, "document": doc.page_content})
        grade = score["score"]
        # Add relevant documents to filtered_docs
        if grade.lower() == "yes":
            print("---GRADE: DOCUMENT RELEVANT")
            filtered_docs.append(doc)
        else:
            print("GRADE: DOCUMENT NOT RELEVANT")
            web_search = "Yes"
            continue
    return {"documents": filtered_docs, "question": question, "web_search": web_search}

