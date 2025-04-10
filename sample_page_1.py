import streamlit as st
import pandas as pd

# 1. 초기 로그 설정
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "history" not in st.session_state:
    st.session_state.history = []

# 2. 필요한 데이터 집계

# 데이터프레임 불러오기
df = pd.read_csv("https://raw.githubusercontent.com/SKNETWORKS-FAMILY-AICAMP/SKN13-1st-4Team/refs/heads/database/DB/car_ins.csv")

# 할인율 범위로 보여줘야 되니까 최댓값 최솟값 모으기기
min_category = []
max_category = []

for category in df['구분'].unique():
    min_value = df[df["구분"] == category]['할인율(%)ascdesc'].min()
    max_value = df[df["구분"] == category]['할인율(%)ascdesc'].max()
    min_category.append(min_value)
    max_category.append(max_value)

# 함수: 페이지 이동
 
# 해당 페이지로 이동(forward)
def go_to(page: str) -> None:
    st.session_state.history.append(st.session_state.current_page)
    st.session_state.current_page = page

# 이전 페이지로 이동(backward)
def go_back()   -> None:
    if st.session_state.current_page != "home":
        st.session_state.current_page = st.session_state.history.pop()    

# 함수: 이미지 to URL 버튼 구현 $$$샘플입니다.$$$
# 일단 이미지는 삼성 로고랑, ULR은 네이버 도메인으로 임의로 설정했어요. 기호에 맞게 사용하면 되려나..?
def samsung_button():
    st.markdown("""
        <a href="https://www.naver.com" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Samsung_Logo.svg/512px-Samsung_Logo.svg.png"
                 alt="삼성화재"
                 style="width:200px; height:auto; margin: 10px 0;">
        </a>
    """, unsafe_allow_html=True)

# 함수: 페이지 구현

# 홈
def home():
    st.title("자동차보험특약정보시스템")
    st.subheader("여러 회사의 자동차 보험 특별 약관을 종류별로 보여줍니다.")

    st.markdown("""
        <style>
        div[data-testid="stButton"] > button {
            width: 300px;
            height: 60px;
            font-size: 30px;
            font-weight: bold;
            border-radius: 12px;
            background-color: #FFFFFF;
            color: black;
            margin: 10px 0;
        }

        div[data-testid="stButton"] > button:hover {
            background-color: #f0f0f0;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)

    left_col, right_col = st.columns(2)
    with left_col:
        st.button("구분별 조회", on_click = lambda: go_to("구분별 페이지"))
        st.caption("예) 자녀할인, 블랙박스장착할인")
    with right_col:
        st.button("보험사별 조회", on_click = lambda: go_to("보험사별 페이지"))
        st.caption("예) DB손해보험, 삼성화재")

    samsung_button()

# 보험사선택: 
def select_company():
    pass

# 구분선택: 
def select_condition():
    st.title("조회하고 싶은 특약 사항 종류를 선택해주세요.")
    st.button(f"자녀할인: {min_category[0]}% ~ {max_category[0]}%",
               on_click = lambda: go_to("자녀할인 페이지"))
    st.button(f"블랙박스장착할인: {min_category[1]}% ~ {max_category[1]}%",
               on_click = lambda: go_to("블랙박스장착할인 페이지"))
    st.button(f"마일리지(후정산형)할인: {min_category[2]}% ~ {max_category[2]}%", 
              on_click = lambda: go_to("마일리지(후정산형)할인 페이지"))
    st.button(f"차선이탈경고(방지)장치할인: {min_category[3]}% ~ {max_category[3]}%", 
              on_click = lambda: go_to("차선이탈경고(방지)장치할인 페이지"))
    st.button(f"고령자안전교육이수할인: {min_category[4]}% ~ {max_category[4]}%", 
              on_click = lambda: go_to("고령자안전교육이수할인 페이지"))
    st.button(f"서민(나눔)우대할인: {min_category[5]}% ~ {max_category[5]}%", 
              on_click = lambda: go_to("서민(나눔)우대할인 페이지"))


# 구분별: 6개

def child_dc():
    st.title(f"자녀할인: 총 {len(df[df['구분']=='자녀할인'])}개")
    st.subheader(f"할인율: {min_category[0]}% ~ {max_category[0]}%")

    right_col, center_col, left_col = st.columns(3)
    with right_col:
        for i in df['회사명'].unique()[:4]:
            st.button(i, on_click = lambda i=i: go_to(f"자녀할인_{i} 페이지"))
    with center_col:
        for i in df['회사명'].unique()[4:8]:
            st.button(i, on_click = lambda i=i: go_to(f"자녀할인_{i} 페이지"))
    with left_col:
        for i in df['회사명'].unique()[8:]:
            st.button(i, on_click = lambda i=i: go_to(f"자녀할인_{i} 페이지"))

def blackbox_dc():
    st.title(f"블랙박스장치할인: 총 {len(df[df['구분']=='블랙박스장착할인'])}개")
    st.subheader(f"할인율: {min_category[1]}% ~ {max_category[1]}%")
 
    right_col, center_col, left_col = st.columns(3)
    with right_col:
        for i in df['회사명'].unique()[:4]:
            st.button(i, on_click = lambda i=i: go_to(f"블랙박스장착할인_{i} 페이지"))
    with center_col:
        for i in df['회사명'].unique()[4:8]:
            st.button(i, on_click = lambda i=i: go_to(f"블랙박스장착할인_{i} 페이지"))
    with left_col:
        for i in df['회사명'].unique()[8:]:
            st.button(i, on_click = lambda i=i: go_to(f"블랙박스장착할인_{i} 페이지"))

def mileage_dc():
    st.title(f"마일리지(후정산형)할인: 총 {len(df[df['구분']=='마일리지(후정산형)할인'])}개")
    st.subheader(f"할인율: {min_category[2]}% ~ {max_category[2]}%")

    right_col, center_col, left_col = st.columns(3)
    with right_col:
        for i in df['회사명'].unique()[:4]:
            st.button(i, on_click = lambda i=i: go_to(f"마일리지(후정산형)할인_{i} 페이지"))
    with center_col:
        for i in df['회사명'].unique()[4:8]:
            st.button(i, on_click = lambda i=i: go_to(f"마일리지(후정산형)할인_{i} 페이지"))
    with left_col:
        for i in df['회사명'].unique()[8:]:
            st.button(i, on_click = lambda i=i: go_to(f"마일리지(후정산형)할인_{i} 페이지"))

def ldws_dc():
    st.title(f"차선이탈경고(방지)장치할인: 총 {len(df[df['구분']=='차선이탈경고(방지)장치할인'])}개")
    st.subheader(f"할인율: {min_category[3]}% ~ {max_category[3]}%")

    right_col, center_col, left_col = st.columns(3)
    with right_col:
        for i in df['회사명'].unique()[:4]:
            st.button(i, on_click = lambda i=i: go_to(f"차선이탈경고(방지)장치할인_{i} 페이지"))
    with center_col:
        for i in df['회사명'].unique()[4:8]:
            st.button(i, on_click = lambda i=i: go_to(f"차선이탈경고(방지)장치할인_{i} 페이지"))
    with left_col:
        for i in df['회사명'].unique()[8:]:
            st.button(i, on_click = lambda i=i: go_to(f"차선이탈경고(방지)장치할인_{i} 페이지"))

def elderly_lecture_dc():
    st.title(f"고령자안전교육이수할인: 총 {len(df[df['구분']=='고령자안전교육이수할인'])}")
    st.subheader(f"할인율: {min_category[4]}% ~ {max_category[4]}%")

    right_col, center_col, left_col = st.columns(3)
    with right_col:
        for i in df['회사명'].unique()[:4]:
            st.button(i, on_click = lambda i=i: go_to(f"고령자안전교육이수할인_{i} 페이지"))
    with center_col:
        for i in df['회사명'].unique()[4:8]:
            st.button(i, on_click = lambda i=i: go_to(f"고령자안전교육이수할인_{i} 페이지"))
    with left_col:
        for i in df['회사명'].unique()[8:]:
            st.button(i, on_click = lambda i=i: go_to(f"고령자안전교육이수할인_{i} 페이지"))

def commoner_dc():
    st.title(f"서민(나눔)우대할인: 총 {len(df[df['구분']=='서민(나눔)우대할인'])}")
    st.subheader(f"할인율: {min_category[5]}% ~ {max_category[5]}%")

    right_col, center_col, left_col = st.columns(3)
    with right_col:
        for i in df['회사명'].unique()[:4]:
            st.button(i, on_click = lambda i=i: go_to(f"서민(나눔)우대할인_{i} 페이지"))
    with center_col:
        for i in df['회사명'].unique()[4:8]:
            st.button(i, on_click = lambda i=i: go_to(f"서민(나눔)우대할인_{i} 페이지"))
    with left_col:
        for i in df['회사명'].unique()[8:]:
            st.button(i, on_click = lambda i=i: go_to(f"서민(나눔)우대할인_{i} 페이지"))

# 이제 6 * 12 = 72개의 하위 페이지 함수를 만들면 되겠군요....!
def dynamic_detail_page():
    page_name = st.session_state.current_page
    # 예: "자녀할인_삼성화재 페이지" → ["자녀할인", "삼성화재 페이지"]
    category, company = page_name.replace(" 페이지", "").split("_")

    st.title(f"{category} - {company}")

    filtered_df = df[(df["구분"] == category) & (df["회사명"] == company)]
    with st.expander("✅ 세부 정보 보기"):
        for idx, row in filtered_df.iterrows():
            st.markdown("---")
            st.markdown(f"**특약명**: {row.get('특약명', '-')}")
            st.markdown(f"**할인율**: {row['할인율(%)ascdesc']}%")
            st.markdown(f"**가입조건**: {row.get('가입조건', '-')}")
            if "비고" in row:
                st.markdown(f"**비고**: {row['비고']}")
    st.dataframe(filtered_df)


# 뒤로가기는 홈화면에선 보여주지 마세요.
if st.session_state.current_page != "home":
    st.button("⬅️ 뒤로가기", on_click=go_back)

# 딕셔너리에 페이지와 함수 매핑
pages = {
    "home":home,
    "구분별 페이지": select_condition,
    "보험사별 페이지": select_company,
    "자녀할인 페이지": child_dc,
    "블랙박스장착할인 페이지": blackbox_dc,
    "마일리지(후정산형)할인 페이지": mileage_dc,
    '차선이탈경고(방지)장치할인 페이지': ldws_dc, ## lane departure warning system
    '고령자안전교육이수할인 페이지': elderly_lecture_dc,
    '서민(나눔)우대할인 페이지': commoner_dc
}

# dymanic pages 72개를 위한 제한사항입니다.
if st.session_state.current_page in pages:
    pages[st.session_state.current_page]()
else:
    dynamic_detail_page()

# 그냥 커스텀어트리뷰트 current_page랑 history 실시간 조회.
st.write(f"현재 페이지: {st.session_state.current_page}")
st.write(f"페이지 로그 스택 방식으로 저장한 거 보여줄게요: {st.session_state.history}")

