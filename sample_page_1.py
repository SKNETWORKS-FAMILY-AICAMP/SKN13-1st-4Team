import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# 1. 초기 로그 설정
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "history" not in st.session_state:
    st.session_state.history = []

# 2. 필요한 데이터 집계

# 데이터프레임 불러오기
df = pd.read_csv("car_ins_after_prepro.csv")

# 할인율 범위로 보여줘야 되니까 최댓값 최솟값 모으기기
min_category = []
max_category = []

for category in df['구분'].unique():
    min_value = df[df["구분"] == category]['할인율(%)'].min()
    max_value = df[df["구분"] == category]['할인율(%)'].max()
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

    st.title("자동차보험특별약관정보비교시스템")
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
    st.markdown("---")
    st.subheader(f"할인율: {min_category[0]}% ~ {max_category[0]}%")
    st.write("자녀 연령과 운전 범위 제한(한정운전 특별약관) 조건에 따라 보험료를 할인받을 수 있습니다.")
    st.markdown("---")

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
    st.markdown("---")
    st.subheader(f"할인율: {min_category[1]}% ~ {max_category[1]}%")
    st.write("블랙박스 장착 여부, 차령, 차종 조건에 따라 자동차 보험료를 할인받을 수 있습니다.")
    st.markdown("---")

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
    st.markdown("---")
    st.subheader(f"할인율: {min_category[2]}% ~ {max_category[2]}%")
    st.write("주행거리가 짧고, 차종, 보험기간, 주행거리 고지방식 등의 조건을 충족하면 보험료를 할인받을 수 있습니다.")
    st.markdown("---")

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
    st.markdown("---")
    st.subheader(f"할인율: {min_category[3]}% ~ {max_category[3]}%")
    st.write("차선이탈경고 또는 방지 장치가 장착된 차량에 대해, 차령, 차종 조건을 고려하여 보험료가 할인됩니다.")
    st.markdown("---")

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
    st.markdown("---")
    st.subheader(f"할인율: {min_category[4]}% ~ {max_category[4]}%")
    st.write("만 65세 이상 고령 운전자가 도로교통공단의 교통안전교육을 수강하면, 자동차 보험료를 할인받을 수 있습니다.")
    st.markdown("---")

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
    st.markdown("---")
    st.subheader(f"할인율: {min_category[5]}% ~ {max_category[5]}%")
    st.write("경제적 여건이 어려운 기초생활수급자, 중증장애인, 저소득 다자녀 가정, 또는 장애인용 차량을 보유한 경우, 자동차 보험료 할인 혜택을 받을 수 있습니다.")
    st.markdown("---")

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

# 함수: 네이버 블로그 세 개 긁어오기
def get_top_three_reviews(query):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)

    url = f"https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={query}"
    driver.get(url)

    try:                # 10초 간 대기
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.title_link"))
        )
        time.sleep(random.uniform(1.5, 2.5)) 
    except:
        print("❌ 블로그 후기 요소가 나타나지 않았습니다.")
        driver.quit()
        return []
    
    elements = driver.find_elements(By.CSS_SELECTOR, "a.title_link")
    links = [el.get_attribute("href") for el in elements[:3]]

    driver.quit()
    return links

# 이제 6 * 12 = 72개의 하위 페이지 함수를 만들면 되겠군요....!
def dynamic_detail_page():
    page_name = st.session_state.current_page
    # 예: "자녀할인_삼성화재 페이지" → ["자녀할인", "삼성화재 페이지"]
    category, company = page_name.replace(" 페이지", "").split("_")

    st.title(f"{category} - {company}")

    filtered_df = df[(df["구분"] == category) & (df["회사명"] == company)]
    if filtered_df.empty:
        st.warning(f"{company}의 {category}에 해당하는 특약 정보가 없습니다.")
        return
    with st.expander("✅ 세부 정보 보기"):
        for idx, row in filtered_df.iterrows():
            st.markdown("---")
            st.markdown(f"**특약명**: {row.get('특약명', '-')}")
            st.markdown(f"**할인율**: {row['할인율(%)']}%")
            st.markdown(f"**가입조건**: {row.get('가입조건', '-')}")
            if "비고" in row:
                st.markdown(f"**비고**: {row['비고']}")
    # st.dataframe(filtered_df)

    st.markdown("---")
    st.header("📌 보험 관련 포스트 검색")
    user_query = st.text_input(f"{company} 자동차보험의 {category}형 특약에 대해 검색합니다. 키워드를 입력해주세요",
                               placeholder = "예) 후기, 비교, 환급 등")
    search_query = f'"{company}" "{category}" {user_query.strip()}'
    review_links = get_top_three_reviews(search_query)       # 블로그 URL 리스트

    # 리스트 출력
    for i, url in enumerate(review_links, 1):
        st.markdown(f"🔗 {i}: [블로그 보러 가기]({url})")
    

# 뒤로가기는 홈화면에선 보여주지 마세요.
if st.session_state.current_page != "home":
    st.button("⬅️ 뒤로가기", on_click=go_back)

# 딕셔너리에 페이지와 함수 매핑
pages1 = {
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
if st.session_state.current_page in pages1:
    pages1[st.session_state.current_page]()
else:
    dynamic_detail_page()

# 그냥 커스텀어트리뷰트 current_page랑 history 실시간 조회.
st.write(f"현재 페이지: {st.session_state.current_page}")
st.write(f"페이지 로그 스택 방식으로 저장한 거 보여줄게요: {st.session_state.history}")