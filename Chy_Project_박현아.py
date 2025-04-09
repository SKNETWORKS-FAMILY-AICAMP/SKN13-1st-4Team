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
        st.button("DB손해보험", on_click = lambda: go_to("DB손보 페이지"))
        st.button("KB손해보험", on_click = lambda: go_to("KB손보 페이지"))
        
    with col2:    
        st.button("메리츠화재", on_click = lambda: go_to("메리츠화재 페이지"))
        st.button("AXA손해보험", on_click = lambda: go_to("AXA손보 페이지"))
        st.button("한화손해보험", on_click = lambda: go_to("한화손보 페이지"))
        st.button("롯데손해보험", on_click = lambda: go_to("롯데손보 페이지"))

    with col3:
        st.button("MG손해보험", on_click = lambda: go_to("MG손보 페이지"))
        st.button("흥국화재해상", on_click = lambda: go_to("흥국화재 페이지"))
        st.button("하나손해보험", on_click = lambda: go_to("하나손해보험 페이지"))
        st.button("캐롯손해보험", on_click = lambda: go_to("캐롯손해보험 페이지"))


# 보험사 detail 파일 불러오기
import pymysql
import pandas as pd

# DB 연결
conn = pymysql.connect(
    host='127.0.0.1',          # 또는 DB 주소
    user='SKN13',
    password='1111',
    database='car_insurance',
    charset='utf8mb4',         # 한글 깨짐 방지
   # cursorclass=pymysql.cursors.DictCursor  # 딕셔너리 형태로 가져오기
)

# 쿼리 작성
query = "SELECT * FROM car_number"

# pandas로 DataFrame 불러오기
insurance_detail = pd.read_sql(query, conn)

df = pd.read_csv("car_ins.csv")

# 대표번호 불러오기
def number(int):
    number = insurance_detail[['회사명', '대표번호']]
    return number.iloc[int,1]

# 상담센터 url 불러오기
def consult(int):
    url = insurance_detail[['상담센터', '민원창구']]
    return url.iloc[int,0]

# 민원창구 url 불러오기
def complain(int):
    url = insurance_detail[['상담센터', '민원창구']]
    return url.iloc[int,1]


# 보험사별: 삼성
def samsung():
    st.title("삼성화재")
    st.subheader("대표번호")
    st.text(number(5))
    st.subheader("상담센터")
    st.link_button(consult(5), consult(5))
    st.subheader("민원창구")
    st.link_button(complain(5), complain(5))
    for i in df['구분'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"삼성화재_{i} 페이지"))

    
# 보험사별: 현대
def hyundai():
    st.title("현대해상")
    st.subheader("대표번호")
    st.text(number(6))
    st.subheader("상담센터")
    st.link_button(consult(6), consult(6))
    st.subheader("민원창구")
    st.link_button(complain(6), complain(6)) 
    for i in df['구분'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"현대해상_{i} 페이지"))

# 보험사별: DB
def db_insu():
    st.title("DB손해보험")
    st.subheader("대표번호")
    st.text(number(8))
    st.subheader("상담센터")
    st.link_button(consult(8), consult(8))
    st.subheader("민원창구")
    st.link_button(complain(8), complain(8))
    for i in df['구분'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"DB손보_{i} 페이지"))

# 보험사별: KB손보
def kb_insu(): 
    st.title("KB손해보험")
    st.subheader("대표번호")
    st.text(number(7))
    st.subheader("상담센터")
    st.link_button(consult(7), consult(7))
    st.subheader("민원창구")
    st.link_button(complain(7), complain(7))
    for i in df['구분'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"KB손보_{i} 페이지"))

# 보험사별: meritz
def meritz():
    st.title("메리츠화재보험")
    st.subheader("대표번호")
    st.text(number(0))
    st.subheader("상담센터")
    st.link_button(consult(0), consult(0))
    st.subheader("민원창구")
    st.link_button(complain(0), complain(0))
    for i in df['구분'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"메리츠화재_{i} 페이지"))

# 보험사별: AXA손보
def AXA():
    st.title("AXA손해보험")
    st.subheader("대표번호")
    st.text(number(9))
    st.subheader("상담센터")
    st.link_button(consult(9), consult(9))
    st.subheader("민원창구")
    st.link_button(complain(9), complain(9))
    for i in df['구분'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"AXA손보_{i} 페이지"))

# 보험사별: 한화
def hanhwa():
    st.title("한화손해보험")
    st.subheader("대표번호")
    st.text(number(1))
    st.subheader("상담센터")
    st.link_button(consult(1), consult(1))
    st.subheader("민원창구")
    st.link_button(complain(1), complain(1))
    for i in df['구분'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"한화손보_{i} 페이지"))

# 보험사별: 롯데
def lotte():
    st.title("롯데손해보험")
    st.subheader("대표번호")
    st.text(number(2))
    st.subheader("상담센터")
    st.link_button(consult(2), consult(2))
    st.subheader("민원창구")
    st.link_button(complain(2), complain(2)) 
    for i in df['구분'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"롯데손보_{i} 페이지"))
        
# 보험사별: MG
def MG():
    st.title("MG손해보험")
    st.subheader("대표번호")
    st.text(number(3))
    st.subheader("상담센터")
    st.link_button(consult(3), consult(3))
    st.subheader("민원창구")
    st.link_button(complain(3), complain(3)) 
    for i in df['구분'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"MG손보_{i} 페이지"))

# 보험사별: 흥국
def heungkuk():
    st.title("흥국화재")
    st.subheader("대표번호")
    st.text(number(8))
    st.subheader("상담센터")
    st.link_button(consult(8), consult(8))
    st.subheader("민원창구")
    st.link_button(complain(8), complain(8))
    for i in df['구분'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"흥국화재_{i} 페이지"))

# 보험사별: 하나손해보험
def hana():
    st.title("하나손해보험")
    st.subheader("대표번호")
    st.text(number(10))
    st.subheader("상담센터")
    st.link_button(consult(10), consult(10))
    st.subheader("민원창구")
    st.link_button(complain(10), complain(10))
    for i in df['구분'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"하나손해보험_{i} 페이지"))

# 보험사별: 캐롯손해보험
def carrot():
    st.title("캐롯손해보험")
    st.subheader("대표번호")
    st.text(number(11))
    st.subheader("상담센터")
    st.link_button(consult(11), consult(11))
    st.subheader("민원창구")
    st.link_button(complain(11), complain(11))
    for i in df['구분'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"캐롯손해보험_{i} 페이지"))

def dynamic_detail_page():
    page_name = st.session_state.current_page
    company, category = page_name.replace(" 페이지", "").split("_")
    
    st.title(f"{company} - {category}")

        # 필터링된 DataFrame 가져오기
    # filtered_df = df[['회사명', '구분']]
    
    filtered_df = df[(df["회사명"] == company) & (df["구분"] == category)]
    with st.expander("✅ 세부 정보 보기"):
        # for idx, row in df.iterrows():
        for idx, row in filtered_df.iterrows():
            st.markdown("---")
            st.markdown(f"**특약명**: {row.get('특약명', '-')}")
            st.markdown(f"**할인율**: {row.get('할인율(%)ascdesc', '-') }%")
            st.markdown(f"**가입조건**: {row.get('가입조건', '-')}")
            if "비고" in row:
                st.markdown(f"**비고**: {row['비고']}")



# 딕셔너리에 페이지와 함수 매핑
pages = {
    "home":home,
    "구분별 페이지": select_condition,
    "보험사별 페이지": select_company,
    "삼성화재 페이지": samsung,
    "현대해상 페이지": hyundai,
    "DB손보 페이지": db_insu,
    "KB손보 페이지": kb_insu,
    "메리츠화재 페이지": meritz,
    "AXA손보 페이지": AXA,
    "한화손보 페이지": hanhwa,
    "롯데손보 페이지": lotte,
    "MG손보 페이지":   MG,
    "흥국화재 페이지": heungkuk,
    "하나손해보험 페이지": hana,
    "캐롯손해보험 페이지": carrot
}

# dymanic pages 72개를 위한 제한사항입니다.
if st.session_state.current_page in pages:
    pages[st.session_state.current_page]()
else:
    dynamic_detail_page()

# pages라는 딕셔너리에서 key로 value 불러오기 -> 함수 호출
# pages[st.session_state.current_page]()

# 뒤로가기는 홈화면에선 보여주지 마세요.
if st.session_state.current_page != "home":
    st.button("⬅", on_click=go_back)


# 그냥 커스텀어트리뷰트 current_page랑 history 실시간 조회.
st.write(f"현재 페이지: {st.session_state.current_page}")
st.write(f"페이지 로그 스택 방식으로 저장한 거 보여줄게요: {st.session_state.history}")