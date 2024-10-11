# backend -> fastapi 를 띄우는 용도.
# app.py는 stream lit으로 frontend를 만드는 용도
import streamlit as st 
import requests

st.title("광고문구 작성 서비스 ✨")

generate_ad_slogan_url = "http://localhost:8000/create_ad_slogan"

product_name = st.text_input("제품 이름")
details = st.text_input("주요 내용")
options = st.multiselect("광고 문구의 톤앤 매너", options=["기본","과장스럽게","차분한","웃긴"], default=["기본"])

# 버튼을 누르면 백엔드로 요청을 보낸다. 
# requests가 요청을 보내는 역할을 한다.
if st.button("광고 문구 생성"):
    try:
        response = requests.post(generate_ad_slogan_url,
                                 json={"product_name": product_name,
                                       "details": details, 
                                       "tone_and_manner":', '.join(options)})
        ad_slogan = response.json()['ad_slogan']
        st.success(ad_slogan)
        
    except:
        st.error("예상치 못한 에러 발생.")