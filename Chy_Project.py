import streamlit as st
import numpy as np
import pandas as pd

import streamlit as st


# 초기 로그 설정
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "history" not in st.session_state:
    st.session_state.history = []

# 함수: 페이지 이동
 
# 해당 페이지로 이동(forward)
def go_to(page: str) -> None:
    st.session_state.history.append(st.session_state.current_page)
    st.session_state.current_page = page

# 이전 페이지로 이동(backward)
def go_back()   -> None:
    if st.session_state.current_page != "home":
        st.session_state.current_page = st.session_state.history.pop()    

# 함수: 페이지 구현

# 홈
def home():
    st.title("자동자보험정보시스템")
    left_col, right_col = st.columns(2)
    with left_col:
        st.button("구분별 조회", on_click = lambda: go_to("구분별 페이지"))
    with right_col:
        st.button("보험사별 조회", on_click = lambda: go_to("보험사별 페이지"))

# 구분별: 일단 기능 구현 안해서 pass로 설정했습니다.
def select_condition():
    pass

# 보험사별
def select_company():
    st.title("보험사를 선택해주세요.")
    
    col1, col2, col3 = st.columns(3)

    # cols = st.colums(2)

    with col1:
        st.button("삼성화재", on_click = lambda: go_to("삼성화재 페이지"))
        st.button("현대해상", on_click = lambda: go_to("현대해상 페이지"))
        st.button("DB손해보험", on_click = lambda: go_to("DB손해보험 페이지"))
        st.button("KB손해보험", on_click = lambda: go_to("KB손해보험 페이지"))
        
    with col2:    
        st.button("메리츠화재", on_click = lambda: go_to("메리츠화재 페이지"))
        st.button("AXA손해보험", on_click = lambda: go_to("AXA손해보험 페이지"))
        st.button("한화손해보험", on_click = lambda: go_to("한화손해보험 페이지"))
        st.button("롯데손해보험", on_click = lambda: go_to("롯데손해보험 페이지"))

    with col3:
        st.button("MG손해보험", on_click = lambda: go_to("MG손해보험 페이지"))
        st.button("흥국화재해상", on_click = lambda: go_to("흥국화재해상 페이지"))
        st.button("하나손해보험", on_click = lambda: go_to("하나손해보험 페이지"))
        st.button("캐롯손해보험", on_click = lambda: go_to("캐롯손해보험 페이지"))

# 보험사별: 삼성
def samsung():
    st.title("삼성화재")

# 보험사별: 현대
def hyundai():
    st.title("현대해상")

# 보험사별: DB
def db_insu():
    st.title("DB손해보험")

# 보험사별: KB손보
def kb_insu(): 
    st.title("KB손해보험")

# 보험사별: 메리츠화재
def meritz():
    st.title("메리츠화재")

# 보험사별: AXA손보
def AXA():
    st.title("AXA손해보험")

# 보험사별: 한화손해보험
def hanhwa():
    st.title("한화손해보험")

# 보험사별: 롯데손해보험
def lotte():
    st.title("롯데손해보험")

# 보험사별: MG손해보험
def MG():
    st.title("MG손해보험")

# 보험사별: 흥국화재해상
def heungkuk():
    st.title("흥국화재해상")

# 보험사별: 하나손해보험
def hana():
    st.title("하나손해보험")

# 보험사별: 캐롯손해보험
def carrot():
    st.title("캐롯손해보험")

# 딕셔너리에 페이지와 함수 매핑
pages = {
    "home":home,
    "구분별 페이지": select_condition,
    "보험사별 페이지": select_company,
    "삼성화재 페이지": samsung,
    "현대해상 페이지": hyundai,
    "DB손해보험 페이지": db_insu,
    "KB손해보험 페이지": kb_insu,
    "메리츠화재 페이지": meritz,
    "AXA손해보험 페이지": AXA,
    "한화손해보험 페이지": hanhwa,
    "롯데손해보험 페이지": lotte,
    "MG손해보험 페이지":   MG,
    "흥국화재해상 페이지": heungkuk,
    "하나손해보험 페이지": hana,
    "캐롯손해보험 페이지": carrot
}

# pages라는 딕셔너리에서 key로 value 불러오기 -> 함수 호출
pages[st.session_state.current_page]()

# 뒤로가기는 홈화면에선 보여주지 마세요.
if st.session_state.current_page != "home":
    st.button("⬅", on_click=go_back)


# 그냥 커스텀어트리뷰트 current_page랑 history 실시간 조회.
st.write(f"현재 페이지: {st.session_state.current_page}")
st.write(f"페이지 로그 스택 방식으로 저장한 거 보여줄게요: {st.session_state.history}")