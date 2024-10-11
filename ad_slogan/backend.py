# fastapi -> 백엔드 이면서도, openai를 감싸는것임. 비지니스 로직이 들어가도록 만들어짐. 
# streamlit -> 서비스 사용하도록
# openai api 활용하여 만든 광고 문구 작성 함수를 호출

import openai
from pydantic import BaseModel
from fastapi import FastAPI

openai.api_key = ""

# 클래스로 openai 를 감싸고자 함. 
class SloganGenerator:
    def __init__(self, engine='gpt-3.5-turbo'):
        self.engine = engine
        self.infer_type = self._get_infer_type_by_engine(engine)
        
    def _get_infer_type_by_engine(self, engine):
        if engine.startswith("text-"):
            return 'completion'
        elif engine.startswith("gpt-"):
            return 'chat'
        
        raise Exception(f"Unknown engine type: {engine}") # 에러를 발생시키는 것.
    
    def _infer_using_completion(self, prompt):
        response = openai.chat.completions.create(engine=self.engine,
                                                  prompt=prompt,
                                                  max_tokens=200,
                                                  n=1)
        result = response.choices[0].text.strip()
        return result
    
    def _infer_using_chatgpt(self, prompt):
        system_instruction = "assistant는 마케팅 문구 작성 도우미로 동작한다. user의 내용을 참고하여 마케팅 문구를 작성해라."
        messages = [{"role":"system", "content":system_instruction},
                    {"role":"user", "content":prompt }]
        response = openai.chat.completions.create(model=self.engine, messages=messages)
        result = response.choices[0].message.content
        
        return result
    
    def generate(self, product_name, details, tone_and_manner):
        prompt = f"제품 이름: {product_name}\n주요내용: {details}\n광고 문구의 스타일: {tone_and_manner}"
        if self.infer_type == 'completion':
            result = self._infer_using_completion(prompt=prompt)
        elif self.infer_type == 'chat':
            result = self._infer_using_chatgpt(prompt=prompt)
        
        return result

# 우리가 흔하게 사용하는 ! 코드 !
# slogan_generator = SloganGenerator(engine='gpt-3.5-turbo')
# result = slogan_generator.generate(product_name="나이키", details="예쁘고 굽이 높음", tone_and_manner="애교쟁이")
# print(result)

# fastapi로 서빙을 해보자 ! 
app = FastAPI()

# 클래스를 포스트로 보내버려서 api 를 만들자. 
class Product(BaseModel):
    product_name: str
    details: str
    tone_and_manner: str

@app.post("/create_ad_slogan")
def create_ad_slogan(product: Product):
    slogan_generator = SloganGenerator('gpt-3.5-turbo')
    
    ad_slogan = slogan_generator.generate(product_name=product.product_name,
                                          details=product.details,
                                          tone_and_manner=product.tone_and_manner)
    return {"ad_slogan": ad_slogan}


"""
fast api 띄우는 법 : 
>> uvicorn backend:app --reload 

백엔드로 서버를 띄운거임. 
swagger를 통해 ui로 접근 가능함. 
"""