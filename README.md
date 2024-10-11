##   🌐 AI 서비스 구현
![image](https://github.com/user-attachments/assets/fc47631b-e69b-43d6-8333-9a0fd0664135)

## 👉 openAI
openAI의 API로 AI 모델을 사용함. 

클라이언트가 서버로 요청을 보내면 그 요청을 openAI에 보내 값을 리턴 받아 프론트 엔드로 제공.

openAI 사용시 계정과 api_key가 필요함.

## 👉 Streamlit
프론트엔드를 구축할 수 있는 오픈소스 프레임워크


- 설치

  ```
  pip install streamlit
  ```

- 실행
  ```
  streamlit run app.py
  ```

## 👉 FastAPI
파이썬으로 API를 빌드할 수 있는 웹 프레임워크

uvicorn 을 통해서 동기, 비동기 처리를 효율적으로 수행함. 

uvicorn [파이썬 파일 이름]:app 으로 서버를 띄울 수 있음.

- 설치

  ```
  pip install fastapi
  pip install uvicorn
  ```

- 서버 실행

  ```
  uvicorn backend:app --reload
  ```
- Swagger UI 확인

  http://127.0.0.1:8000/model/docs#/
