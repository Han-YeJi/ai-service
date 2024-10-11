import openai
from pydantic import BaseModel
from fastapi import FastAPI

openai.api_key = ""

def summarize(text):
    system_instruction = "assistant는 user의 입력을 bullet point로 3줄 요약해준다."
    
    messages = [{"role": "system", "content": system_instruction},
                {"role": "user", "content": text}]
    
    response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    result = response.choices[0].message.content
    return result

app = FastAPI()

class InputText(BaseModel):
    text: str
    
@app.post("/summarize")
def post_summarize(input_text: InputText):
    summary = summarize(input_text.text)
    return {"summary": summary}


# 서버 띄워서 swagger로 확인 가능 
# uvicorn backend:app --reload