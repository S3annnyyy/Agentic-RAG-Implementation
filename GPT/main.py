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

    # 1. Initialize schema
    #TODO
    # 2. Retrieve frontend request from body
    #TODO
    # 3. Initialize openai chat completions instance with gpt-3.5-turbo model
    # 4. Show what happens if exceed token limit, unable to close json then give error
    #TODO
    
    return jsonResponse(200, response="Not implemented yet")


if __name__ == "__main__":   
   app.run(host='0.0.0.0', port=8000, debug=True)