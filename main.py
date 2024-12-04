#pip install python-dotenv
#pip install langchain-openai
#pip install streamlit

# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

# subject = "AI"
# result = chat_model.invoke(subject + "에 대한 시를 써 줘")
# print(result.content)

import streamlit as st

st.title("인공지능 시인") #홈페이지 제목
subject = st.text_input("시의 주제를 입력해주세요.") #input 받을 텍스트 받을 변수
st.write("시의 주제: " + subject) #입력받은 값을 홈페이지에 출력해줌

#버튼을 눌러서 작동하도록 함 (이 과정을 진행 안 하면 그냥 엔터만 눌러도 시를 작성해줌)
if st.button("시 작성"):
    with st.spinner("시 작성중"): #로딩이 될 동안 로딩이모티콘을 띄워줌
        result = chat_model.invoke(subject + "에 대한 시를 써줘.")
        st.write(result.content) # result는 LLM이 출력하는 모든 값이 나오므로(추론 등), 그 내용만 얻으려면 .content를 해주어야 함 

