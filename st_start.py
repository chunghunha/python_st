import streamlit as st  # streamlit 라이브러리 임포트

# 타이틀 텍스트 출력
st.title('첫번째 웹 어플 만들기 👋📺🙉')

st.write('# 1. Markdown 텍스트 작성하기')
st.write('# 2. 텍스트 작성하기')

import pandas as pd  # pandas 라이브러리 임포트

st.write('# 2. DataFrame 표시하기')  # 텍스트 출력
df = pd.DataFrame({  # DataFrame 생성
    '이름': ['홍길동', '이순신', '강감찬'],
    '나이': [20, 45, 35]
})

st.dataframe(df)  # DataFrame 출력