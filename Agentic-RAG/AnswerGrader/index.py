from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate

LLM = ChatOllama(model="llama3", format="json", temperature=0)
PROMPT = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a grader assessing 
    whether an answer is useful to resolve a question. Give a binary score 'yes' or 'no' to indicate 
    whether the answer is useful to resolve a question. Provide the binary score as a JSON with a 
    single key 'score' and no preamble or explanation. <|eot_id|><|start_header_id|>user<|end_header_id|> 
    Here is the answer: {generation}
    -----
    Here is the question: {question} <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
    input_variables=["generation", "question"],
)

def answerGrader(answerGenerated, docs):
    """
    """
    aGrader = PROMPT | LLM | JsonOutputParser()
    outcome = aGrader.invoke({"question": docs, "generation": answerGenerated}) 
    return outcome