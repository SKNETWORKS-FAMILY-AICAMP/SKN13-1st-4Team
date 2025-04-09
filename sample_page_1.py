import streamlit as st
import pandas as pd

# 1. 초기 로그 설정
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "history" not in st.session_state:
    st.session_state.history = []

# 2. 필요한 데이터 집계

# 데이터프레임 불러오기
df = pd.read_csv("insurance_info.csv")

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



# 함수: 페이지 구현

# 홈
def home():
    st.title("자동자보험정보시스템")
    left_col, right_col = st.columns(2)
    with left_col:
        st.button("구분별 조회", on_click = lambda: go_to("구분별 페이지"))
    with right_col:
        st.button("보험사별 조회", on_click = lambda: go_to("보험사별 페이지"))

# 보험사선택: 
def select_company():
    pass

# 구분선택: 
def select_condition():
    st.title("조회하고 싶은 특약 사항 종류를 선택해주세요.")
    st.button("자녀할인", on_click = lambda: go_to("자녀할인 페이지"))
    st.button("블랙박스장착할인", on_click = lambda: go_to("블랙박스장착할인 페이지"))
    st.button("마일리지(후정산형)할인", on_click = lambda: go_to("마일리지(후정산형)할인 페이지"))
    st.button("차선이탈경고(방지)장치할인", on_click = lambda: go_to("차선이탈경고(방지)장치할인 페이지"))
    st.button("고령자안전교육이수할인", on_click = lambda: go_to("고령자안전교육이수할인 페이지"))
    st.button("서민(나눔)우대할인", on_click = lambda: go_to("서민(나눔)우대할인 페이지"))

# 구분별: 6개
def child_dc():
    st.title("자녀할인")
    st.write(f"할인율: {min_category[0]}% ~ {max_category[0]}%")
    for i in df['회사명'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"자녀할인_{i} 페이지"))
def blackbox_dc():
    st.title("블랙박스장착할인")
    st.write(f"할인율: {min_category[1]}% ~ {max_category[1]}%")
    for i in df['회사명'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"블랙박스_{i} 페이지"))
def mileage_dc():
    st.title("마일리지(후정산형)할인")
    st.write(f"할인율: {min_category[2]}% ~ {max_category[2]}%")
    for i in df['회사명'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"마일리지(후정산형)_{i} 페이지"))
def ldws_dc():
    st.title("차선이탈경고(방지)장치할인")
    st.write(f"할인율: {min_category[3]}% ~ {max_category[3]}%")
    for i in df['회사명'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"차선이탈경고(방지)장치할인_{i} 페이지"))
def elderly_lecture_dc():
    st.title("고령자안전교육이수할인")
    st.write(f"할인율: {min_category[4]}% ~ {max_category[4]}%")
    for i in df['회사명'].unique():
        st.button(i, on_click = lambda i=i: go_to(f"고령자안전교육이수할인_{i} 페이지"))
def commoner_dc():
    st.title("서민(나눔)우대할인")
    st.write(f"할인율: {min_category[5]}% ~ {max_category[5]}%")
    for i in df['회사명'].unique():
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


# 뒤로가기는 홈화면에선 보여주지 마세요.
if st.session_state.current_page != "home":
    st.button("⬅", on_click=go_back)

# 딕셔너리에 페이지와 함수 매핑
pages = {
    "home":home,
    "구분별 페이지": select_condition,
    "보험사별 페이지": select_company,
    "자녀할인 페이지": child_dc,
    "블랙박스장착할인 페이지": blackbox_dc,
    "마일리지(후정산형)할인 페이지": mileage_dc,
    '차선이탈경고(방지)장치할인 페이지':  ldws_dc, ## lane departure warning system
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