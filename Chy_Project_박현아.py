import streamlit as st
import numpy as np
import pandas as pd

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time



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
# def home():
#     st.title("자동자보험정보시스템")
#     left_col, right_col = st.columns(2)
#     with left_col:
#         st.button("구분별 조회", on_click = lambda: go_to("구분별 페이지"))
#     with right_col:
#         st.button("보험사별 조회", on_click = lambda: go_to("보험사별 페이지"))

def home():
    st.title("🚗 자동차보험 정보 시스템")
    left_col, right_col = st.columns(2)
    with left_col:
        st.button("구분별 조회", on_click = lambda: go_to("구분별 페이지"))
    with right_col:
        st.button("보험사별 조회", on_click = lambda: go_to("보험사별 페이지"))
    # with middle_col:
    #     st.button("test용", on_click = lambda: go_to("보험사별 페이지"))
        

# 예: details 페이지 처리
page = st.query_params.get("page", "home")
if page == "details":
    st.write("📄 상세 페이지로 이동했습니다!")


insurance_detail = pd.read_csv("car_ins_com_after_prepro.csv")
df = pd.read_csv("car_ins_after_prepro.csv")

# 구분별: 일단 기능 구현 안해서 pass로 설정했습니다.
def select_condition():
    pass

    
# 보험사별


# 할인율 범위로 보여줘야 되니까 최댓값 최솟값 모으기기
min_category = []
max_category = []

for company in df['회사명'].unique():
    min_value = df[df["회사명"] == company]['할인율(%)'].min()
    max_value = df[df["회사명"] == company]['할인율(%)'].max()
    min_category.append(min_value)
    max_category.append(max_value)


def select_company():
    st.title(" 보험사를 선택해주세요.")
    
    col1, col2, col3 = st.columns(3)


    
    with col1:
        st.button("삼성화재", on_click = lambda: go_to("삼성화재해상보험 페이지"))
        st.caption(f"삼성화재: {min_category[5]}% ~ {max_category[5]}%")
        st.button("현대해상화재보험", on_click = lambda: go_to("현대해상화재보험 페이지"))
        st.caption(f"현대해상: {min_category[6]}% ~ {max_category[6]}%")
        st.button("DB손해보험", on_click = lambda: go_to("DB손해보험 페이지"))
        st.caption(f"DB손해보험: {min_category[8]}% ~ {max_category[8]}%")
        st.button("KB손해보험", on_click = lambda: go_to("KB손해보험 페이지"))
        st.caption(f"KB손해보험: {min_category[7]}% ~ {max_category[7]}%") 
        
    with col2:    
        st.button("메리츠화재보험", on_click = lambda: go_to("메리츠화재보험 페이지"))
        st.caption(f"메리츠화재보험: {min_category[0]}% ~ {max_category[0]}%") 
        st.button("AXA손해보험", on_click = lambda: go_to("AXA손해보험 페이지"))
        st.caption(f"AXA손해보험: {min_category[9]}% ~ {max_category[9]}%")
        st.button("한화손해보험", on_click = lambda: go_to("한화손해보험 페이지"))
        st.caption(f"한화손해보험: {min_category[1]}% ~ {max_category[1]}%") 
        st.button("롯데손해보험", on_click = lambda: go_to("롯데손해보험 페이지"))
        st.caption(f"롯데손해보험: {min_category[2]}% ~ {max_category[2]}%")

    with col3:
        st.button("MG손해보험", on_click = lambda: go_to("MG손해보험 페이지"))
        st.caption(f"MG손해보험: {min_category[3]}% ~ {max_category[3]}%")
        st.button("흥국화재해상", on_click = lambda: go_to("흥국화재해상보험 페이지"))
        st.caption(f"흥국화재해상: {min_category[4]}% ~ {max_category[4]}%")
        # st.button("하나손해보험", on_click = lambda: go_to("하나손해보험 페이지"))
        st.button("캐롯손해보험", on_click = lambda: go_to("캐롯손해보험 페이지"))
        st.caption(f"캐롯손해보험: {min_category[10]}% ~ {max_category[10]}%")



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
    st.title("삼성화재해상보험")
    st.markdown("---")
    st.subheader("대표번호")
    st.text(number(5))
    st.subheader("상담센터 및 민원창구 바로가기")
    left_col, right_col = st.columns(2)
    with left_col:
        st.link_button("📞 상담센터 바로가기", consult(5))
    with right_col:
        st.link_button("🧑‍💻 민원창구 바로가기", complain(5))
    st.markdown("---")
    st.subheader("특약 종류")
    left_col, right_col = st.columns(2)
    with left_col:
        for i in df['구분'].unique()[:3]:
            st.button(i, on_click = lambda i=i: go_to(f"삼성화재해상보험_{i} 페이지"))
    with right_col:
        for i in df['구분'].unique()[3:]:
            st.button(i, on_click = lambda i=i: go_to(f"삼성화재해상보험_{i} 페이지"))

    
# 보험사별: 현대
def hyundai():
    st.title("현대해상화재보험")
    st.markdown("---")
    st.subheader("대표번호")
    st.text(number(6))
    st.subheader("상담센터 및 민원창구 바로가기")
    left_col, right_col = st.columns(2)
    with left_col:
        st.link_button("📞 상담센터 바로가기", consult(6))
    with right_col:
        st.link_button("🧑‍💻 민원창구 바로가기", complain(6))
    st.markdown("---")
    st.subheader("특약 종류") 
    left_col, right_col = st.columns(2)
    with left_col:
        for i in df['구분'].unique()[:3]:
            st.button(i, on_click = lambda i=i: go_to(f"현대해상화재보험_{i} 페이지"))
    with right_col:
        for i in df['구분'].unique()[3:]:
            st.button(i, on_click = lambda i=i: go_to(f"현대해상화재보험_{i} 페이지"))

# 보험사별: DB
def db_insu():
    st.title("DB손해보험")
    st.markdown("---")
    st.subheader("대표번호")
    st.text(number(8))
    st.subheader("상담센터 및 민원창구 바로가기")
    left_col, right_col = st.columns(2)
    with left_col:
        st.link_button("📞 상담센터 바로가기", consult(8))
    with right_col:
        st.link_button("🧑‍💻 민원창구 바로가기", complain(8))
    st.markdown("---")
    st.subheader("특약 종류")
    left_col, right_col = st.columns(2)
    with left_col:
        for i in df['구분'].unique()[:3]:
            st.button(i, on_click = lambda i=i: go_to(f"DB손해보험_{i} 페이지"))
    with right_col:
        for i in df['구분'].unique()[3:]:
            st.button(i, on_click = lambda i=i: go_to(f"DB손해보험_{i} 페이지"))

# 보험사별: KB손보
def kb_insu(): 
    st.title("KB손해보험")
    st.markdown("---")
    st.subheader("대표번호")
    st.text(number(7))
    st.subheader("상담센터 및 민원창구 바로가기")
    left_col, right_col = st.columns(2)
    with left_col:
        st.link_button("📞 상담센터 바로가기", consult(7))
    with right_col:
        st.link_button("🧑‍💻 민원창구 바로가기", complain(7))
    st.markdown("---")
    st.subheader("특약 종류")
    left_col, right_col = st.columns(2)
    with left_col:
        for i in df['구분'].unique()[:3]:
            st.button(i, on_click = lambda i=i: go_to(f"KB손해보험_{i} 페이지"))
    with right_col:
        for i in df['구분'].unique()[3:]:
            st.button(i, on_click = lambda i=i: go_to(f"KB손해보험_{i} 페이지"))

# 보험사별: meritz
def meritz():
    st.title("메리츠화재보험")
    st.markdown("---")
    st.subheader("대표번호")
    st.text(number(0))
    st.subheader("상담센터 및 민원창구 바로가기")
    left_col, right_col = st.columns(2)
    with left_col:
        st.link_button("📞 상담센터 바로가기", consult(0))
    with right_col:
        st.link_button("🧑‍💻 민원창구 바로가기", complain(0))
    st.markdown("---")
    st.subheader("특약 종류")
    left_col, right_col = st.columns(2)
    with left_col:
        for i in df['구분'].unique()[:3]:
            st.button(i, on_click = lambda i=i: go_to(f"메리츠화재보험_{i} 페이지"))
    with right_col:
        for i in df['구분'].unique()[3:]:
            st.button(i, on_click = lambda i=i: go_to(f"메리츠화재보험_{i} 페이지"))

# 보험사별: AXA손보
def AXA():
    st.title("AXA손해보험")
    st.markdown("---")
    st.subheader("대표번호")
    st.text(number(9))
    st.subheader("상담센터 및 민원창구 바로가기")
    left_col, right_col = st.columns(2)
    with left_col:
        st.link_button("📞 상담센터 바로가기", consult(9))
    with right_col:
        st.link_button("🧑‍💻 민원창구 바로가기", complain(9))
    st.markdown("---")
    st.subheader("특약 종류")
    left_col, right_col = st.columns(2)
    with left_col:
        for i in df['구분'].unique()[:3]:
            st.button(i, on_click = lambda i=i: go_to(f"AXA손해보험_{i} 페이지"))
    with right_col:
        for i in df['구분'].unique()[3:]:
            st.button(i, on_click = lambda i=i: go_to(f"AXA손해보험_{i} 페이지"))

# 보험사별: 한화
def hanhwa():
    st.title("한화손해보험")
    st.markdown("---")
    st.subheader("대표번호")
    st.text(number(1))
    st.subheader("상담센터 및 민원창구 바로가기")
    left_col, right_col = st.columns(2)
    with left_col:
        st.link_button("📞 상담센터 바로가기", consult(1))
    with right_col:
        st.link_button("🧑‍💻 민원창구 바로가기", complain(1))
    st.markdown("---")
    st.subheader("특약 종류")
    left_col, right_col = st.columns(2)
    with left_col:
        for i in df['구분'].unique()[:3]:
            st.button(i, on_click = lambda i=i: go_to(f"한화손해보험_{i} 페이지"))
    with right_col:
        for i in df['구분'].unique()[3:]:
            st.button(i, on_click = lambda i=i: go_to(f"한화손해보험_{i} 페이지"))

# 보험사별: 롯데
def lotte():
    st.title("롯데손해보험")
    st.markdown("---")
    st.subheader("대표번호")
    st.text(number(2))
    st.subheader("상담센터 및 민원창구 바로가기")
    left_col, right_col = st.columns(2)
    with left_col:
        st.link_button("📞 상담센터 바로가기", consult(2))
    with right_col:
        st.link_button("🧑‍💻 민원창구 바로가기", complain(2))
    st.markdown("---")
    st.subheader("특약 종류") 
    left_col, right_col = st.columns(2)
    with left_col:
        for i in df['구분'].unique()[:3]:
            st.button(i, on_click = lambda i=i: go_to(f"롯데손해보험_{i} 페이지"))
    with right_col:
        for i in df['구분'].unique()[3:]:
            st.button(i, on_click = lambda i=i: go_to(f"롯데손해보험_{i} 페이지"))
        
# 보험사별: MG
def MG():
    st.title("MG손해보험")
    st.markdown("---")
    st.subheader("대표번호")
    st.text(number(3))
    st.subheader("상담센터 및 민원창구 바로가기")
    left_col, right_col = st.columns(2)
    with left_col:
        st.link_button("📞 상담센터 바로가기", consult(3))
    with right_col:
        st.link_button("🧑‍💻 민원창구 바로가기", complain(3))
    st.markdown("---")
    st.subheader("특약 종류") 
    left_col, right_col = st.columns(2)
    with left_col:
        for i in df['구분'].unique()[:3]:
            st.button(i, on_click = lambda i=i: go_to(f"MG손해보험_{i} 페이지"))
    with right_col:
        for i in df['구분'].unique()[3:]:
            st.button(i, on_click = lambda i=i: go_to(f"MG손해보험_{i} 페이지"))

# 보험사별: 흥국
def heungkuk():
    st.title("흥국화재")
    st.markdown("---")
    st.subheader("대표번호")
    st.text(number(4))
    st.subheader("상담센터 및 민원창구 바로가기")
    left_col, right_col = st.columns(2)
    with left_col:
        st.link_button("📞 상담센터 바로가기", consult(4))
    with right_col:
        st.link_button("🧑‍💻 민원창구 바로가기", complain(4))
    st.markdown("---")
    st.subheader("특약 종류")
    left_col, right_col = st.columns(2)
    with left_col:
        for i in df['구분'].unique()[:3]:
            st.button(i, on_click = lambda i=i: go_to(f"흥국화재해상보험_{i} 페이지"))
    with right_col:
        for i in df['구분'].unique()[3:]:
            st.button(i, on_click = lambda i=i: go_to(f"흥국화재해상보험_{i} 페이지"))
            

# # 보험사별: 하나손해보험
# def hana():
#     st.title("하나손해보험")
#     st.subheader("대표번호")
#     st.text(number(10))
#     st.subheader("상담센터")
#     st.link_button(consult(10), consult(10))
#     st.subheader("민원창구")
#     st.link_button(complain(10), complain(10))
#     for i in df['구분'].unique():
#         st.button(i, on_click = lambda i=i: go_to(f"하나손해보험_{i} 페이지"))

# 보험사별: 캐롯손해보험
def carrot():
    st.title("캐롯손해보험")
    st.markdown("---")
    st.subheader("대표번호")
    st.text(number(11))
    st.subheader("상담센터 및 민원창구 바로가기")
    left_col, right_col = st.columns(2)
    with left_col:
        st.link_button("📞 상담센터 바로가기", consult(11))
    with right_col:
        st.link_button("🧑‍💻 민원창구 바로가기", complain(11))
    st.markdown("---")
    st.subheader("특약 종류")
    left_col, right_col = st.columns(2)
    with left_col:
        for i in df['구분'].unique()[:3]:
            st.button(i, on_click = lambda i=i: go_to(f"캐롯손해보험_{i} 페이지"))
    with right_col:
        for i in df['구분'].unique()[3:]:
            st.button(i, on_click = lambda i=i: go_to(f"캐롯손해보험_{i} 페이지"))

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


def dynamic_detail_page():
    page_name = st.session_state.current_page
    company, category = page_name.replace(" 페이지", "").split("_")
    
    st.title(f"{company} - {category}")


    
    # 회사명과 특약 이름별로 구분된 df 만들기
    filtered_df = df[(df["회사명"] == company) & (df["구분"] == category)]
    if filtered_df.empty:
        st.warning(f"{company}의 {category}에 해당하는 특약 정보가 없습니다.")
        return

        
    discount_rate = filtered_df.iloc[:,-1]
    st.write(f"총 {len(discount_rate)}개")
    st.write(f"할인율: {min(discount_rate)} ~ {max(discount_rate)}%")
    if category == '자녀할인':
        st.write("자녀 연령과 운전 범위 제한(한정운전 특별약관) 조건에 따라 보험료를 할인받을 수 있습니다.")
    elif category == '블랙박스장착할인':
        st.write('블랙박스 장착 여부, 차령, 차종 조건에 따라 자동차 보험료를 할인받을 수 있습니다.')
    elif category == '마일리지할인':
        st.write('주행거리가 짧고, 차종, 보험기간, 주행거리 고지방식 등의 조건을 충족하면 보험료를 할인받을 수 있습니다.')
    elif category == '차선이탈경고(방지)장치할인':
        st.write('차선이탈경고 또는 방지 장치가 장착된 차량에 대해, 차령, 차종 조건을 고려하여 보험료가 할인됩니다.')
    elif category == '고령자 안전교육이수할인':
        st.write('만 65세 이상 고령 운전자가 도로교통공단의 교통안전교육을 수강하면, 자동차 보험료를 할인받을 수 있습니다.')
    else:
        st.write('경제적 여건이 어려운 기초생활수급자, 중증장애인, 저소득 다자녀 가정, 또는 장애인용 차량을 보유한 경우, 자동차 보험료 할인 혜택을 받을 수 있습니다.')


    #세부정보
    with st.expander("✅ 세부 정보 보기"):
        # for idx, row in df.iterrows():
        for idx, row in filtered_df.iterrows():
            st.markdown("---")
            st.markdown(f"**특약명**: {row.get('특약명', '-')}")
            st.markdown(f"**할인율**: {row.get('할인율(%)', '-') }%")
            st.markdown(f"**가입조건**: {row.get('가입조건', '-')}")
            if "비고" in row:
                st.markdown(f"**비고**: {row['비고']}")


    st.markdown("---")
    st.header("📌 보험 관련 포스트 검색")
    user_query = st.text_input(f"{company} 자동차보험의 {category}형 특약에 대해 검색합니다. 키워드를 입력해주세요",
                               placeholder = "예) 후기, 비교, 환급 등")
    
    search_query = f'"{company}" "{category}" {user_query.strip()}'

    review_links = get_top_three_reviews(search_query)   
    # st.dataframe(filtered_df) # dataframe 보여주기
    # 블로그 URL 리스트


    # 리스트 출력
    for i, url in enumerate(review_links, 1):
        st.markdown(f"🔗 {i}: [블로그 보러 가기]({url})")

    


# 뒤로가기는 홈화면에선 보여주지 마세요.
if st.session_state.current_page != "home":
    st.button("⬅", on_click=go_back)
    
# 딕셔너리에 페이지와 함수 매핑
pages = {
    "home":home,
    "구분별 페이지": select_condition,
    "보험사별 페이지": select_company,
    "삼성화재해상보험 페이지": samsung,
    "현대해상화재보험 페이지": hyundai,
    "DB손해보험 페이지": db_insu,
    "KB손해보험 페이지": kb_insu,
    "메리츠화재보험 페이지": meritz,
    "AXA손해보험 페이지": AXA,
    "한화손해보험 페이지": hanhwa,
    "롯데손해보험 페이지": lotte,
    "MG손해보험 페이지":   MG,
    "흥국화재해상보험 페이지": heungkuk,
    # "하나손해보험 페이지": hana,
    "캐롯손해보험 페이지": carrot
}

# dymanic pages 72개를 위한 제한사항입니다.
if st.session_state.current_page in pages:
    pages[st.session_state.current_page]()
else:
    dynamic_detail_page()




# 그냥 커스텀어트리뷰트 current_page랑 history 실시간 조회.
st.write(f"현재 페이지: {st.session_state.current_page}")
st.write(f"페이지 로그 스택 방식으로 저장한 거 보여줄게요: {st.session_state.history}")