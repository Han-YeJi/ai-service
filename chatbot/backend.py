import openai
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

openai.api_key = ""

app = FastAPI()
def to_dict_recursive(obj):
    """
    객체를 재귀적으로 딕셔너리로 변환합니다.
    """
    if isinstance(obj, dict):
        return {key: to_dict_recursive(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [to_dict_recursive(item) for item in obj]
    elif hasattr(obj, '__dict__'):
        return {key: to_dict_recursive(value) for key, value in obj.__dict__.items()}
    else:
        return obj
    
def chat(messages):
    response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    
    
    resp_dict = to_dict_recursive(response)
    assistant_turn = resp_dict['choices'][0]['message']
    return assistant_turn 

class Turn(BaseModel):
    role: str
    content: str
    
class Messages(BaseModel):
    messages: List[Turn]

@app.post("/chat", response_model=Turn) # response_model : 어떤식의 응답이 나갈건지 알려줌.
def post_chat(messages: Messages):
    messages = messages.dict()
    assitant_turn = chat(messages=messages['messages'])
    return assitant_turn