"""
Documentation: 
1. https://platform.openai.com/docs/api-reference/chat
2. https://platform.openai.com/docs/api-reference/chat/object 
"""

import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import json
from pprint import pprint
import logging
from openai import OpenAI

load_dotenv()
logging.basicConfig(level=logging.INFO)

OPEN_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPEN_API_KEY)
 
app = Flask(__name__)
CORS(app)

def jsonResponse(rescode, **kwargs):
    res_data = {key: value for key, value in kwargs.items()}
    return jsonify(res_data), rescode


@app.route("/v1/gpt/generate", methods=['POST'])
def generate_response():

    # V1: Showcase basic api calls first before
    # completion = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    # messages=[
    #     {"role": "system", "content": "You are a helpful recipe assistant. Only use the functions you have been provided with"},   
    #     {"role": "system", "content": "You are a helpful assistant designed to output JSON."},             
    #     {"role": "user", "content": "Come up with the recipe for chicken rice with at least 10 steps"},        
    # ],
    # response_format={ "type": "json_object" },    
    # )

    # response = completion.choices[0].message.content    
    
    # return jsonResponse(200, data={"response": json.loads(response)})

    
    # V2: Showcase how to generate consistent responses
    schema = { 
        "type": "object",
            "properties": {
                "dish": {
                    "type": "string",
                    "description": "Descriptive title of the dish"
                },
                "ingredients": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "instructions": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "step": {
                                "type": "integer",
                                "description": "Step number, numbering from 1"
                            },
                            "description": {
                                "type": "string",
                                "description": "Steps to prepare the recipe."
                            }
                        }
                    }
                }
            }
        }
    
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": f"Provide output in valid json format. The data schema should be like this {json.dumps(schema)}"},
            {"role": "system", "content": "You are a helpful recipe assistant. Only use the information you have been provided with"},                            
            {"role": "user", "content": "Come up with the recipe for chicken rice with 3 steps"},       
        ],            
        temperature=0.1,
        # tools=tools,
    )

    data = chat_completion.choices[0].message.content

    # V3: Showcase how to generate consistent responses + show what happens if exceed token limit, unable to close json then give error
    # Finish reason for token exceeding is length else it should be stop
    finish_reason = chat_completion.choices[0].finish_reason
    print(finish_reason)
        
    return jsonResponse(200,data={"response": json.loads(data)})


if __name__ == "__main__":   
   app.run(host='0.0.0.0', port=8000, debug=True)