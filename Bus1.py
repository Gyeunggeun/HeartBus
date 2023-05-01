import pandas as pd
import streamlit as st
import numpy as np
import datetime
import os
import altair as alt


# -------------------- ▲ 필요 변수 생성 코딩 End ▲ --------------------

# 만약 CSV 파일이 없다면, 빈 파일을 생성
if not os.path.exists("상담 학생 데이터.csv"):
    df = pd.DataFrame(columns=["start_date", "start_hour", "start_minute", "name", "age", "gender", "communication", "number", "grade", "relationship", "sex", "bullying", "domestic_violence", "depression", "lifestyle", "addiction", "drugs", "Teenager_counsler", "College_counsler", "Adult_counsler", "additional_text"])
    df.to_csv("상담 학생 데이터.csv", index=False, encoding="utf-8-sig")

# CSV 파일을 불러오기
df = pd.read_csv("상담 학생 데이터.csv")


# -------------------- ▼ Streamlit 웹 화면 구성 START ▼ --------------------

# 레이아웃 구성하기
st.set_page_config('상담 신청 양식 및 대시보드', layout='wide', initial_sidebar_state='expanded')

# tabs 만들기
tab1, tab2, tab3 = st.tabs(['상담 예약 페이지', '상담사 정보 입력','대시보드'])
with tab1:
        # 제목 넣기
        st.markdown("## 상담 예약 페이지")

        # 시간 정보 가져오기
        now_date = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=9)

        # 환자정보 널기
        st.markdown("#### 여기에 정보를 입력하세요")


        ## -------------------- ▼ 1-1그룹 날짜/시간 입력 cols 구성(출동일/날짜정보(input_date)/출동시간/시간정보(input_time)) ▼ --------------------

        col110, col111, col112, col113, col114 = st.columns([0.1, 0.3, 0.1, 0.15, 0.15])
        with col110:
            with st.container():
                st.markdown(
                    f'<div style="height: 72px; line-height: 62px; background-color:#C8EFF2 ; font-family: Malgun Gothic; white-space: pre-wrap; overflow-wrap: break-word; padding: 0 1.0rem; border: 1px solid #f0f2f6; border-radius:5px;">{"희망 상담 일시"}</div>',
                    unsafe_allow_html=True,
                )

        with col111:
            start_date = st.date_input("희망 상담 일시", datetime.date.today())
        with col112:
            with col112:
                with st.container():
                    st.markdown(
                        f'<div style="height: 72px; line-height: 62px; background-color:#C8EFF2 ; font-family: Malgun Gothic; white-space: pre-wrap; overflow-wrap: break-word; padding: 0 1.0rem; border: 1px solid #f0f2f6; border-radius:5px;">{"희망 상담 시간"}</div>',
                        unsafe_allow_html=True,
                    )
        with col113:
            start_hour = st.selectbox('시각', list(i for i in range(0,24)))
        with col114:
            start_minute = st.selectbox('분', list(i for i in range(0, 60, 30)))


        ## -------------------------------------------------------------------------------------
        col120, col121, col122, col123, col124, col125 = st.columns([0.1, 0.3, 0.1, 0.1, 0.1, 0.1])
        with col120:
            with st.container():
                st.markdown(
                    f'<div style="height: 72px; line-height: 62px; background-color:#C8EFF2 ; font-family: Malgun Gothic; white-space: pre-wrap; overflow-wrap: break-word; padding: 0 1.0rem; border: 1px solid #f0f2f6; border-radius:5px;">{"닉네임"}</div>',
                    unsafe_allow_html=True,
                )
        with col121:
            name = st.text_input("닉네임을 입력하세요")
        with col122:
            with st.container():
                st.markdown(
                    f'<div style="height: 72px; line-height: 62px; background-color:#C8EFF2 ; font-family: Malgun Gothic; white-space: pre-wrap; overflow-wrap: break-word; padding: 0 1.0rem; border: 1px solid #f0f2f6; border-radius:5px;">{"나이"}</div>',
                    unsafe_allow_html=True,
                )
        with col123:
            age = st.number_input("나이를 입력하세요", min_value=0, max_value=150, step=1)
        with col124:
            with st.container():
                st.markdown(
                    f'<div style="height: 72px; line-height: 62px; background-color:#C8EFF2 ; font-family: Malgun Gothic; white-space: pre-wrap; overflow-wrap: break-word; padding: 0 1.0rem; border: 1px solid #f0f2f6; border-radius:5px;">{"성별"}</div>',
                    unsafe_allow_html=True,
                )
        with col125:
            gender = st.radio("성별을 선택하세요", ["남성", "여성"], horizontal=True)

        ## -------------------- ▼ 1-3그룹 체온/환자위치(주소) 입력 cols 구성(체온/체온 숫자 입력(fever)/환자 위치/환자위치 텍스트 입력(location)) ▼ --------------------

        col130, col131, col132, col133 = st.columns([0.1, 0.3, 0.1, 0.3])  # col 나누기
        with col130:
            with st.container():
                st.markdown(
                    f'<div style="height: 72px; line-height: 62px; background-color:#C8EFF2 ; font-family: Malgun Gothic; white-space: pre-wrap; overflow-wrap: break-word; padding: 0 1.0rem; border: 1px solid #f0f2f6; border-radius:5px;">{"연락 수단"}</div>',
                    unsafe_allow_html=True,
                )
        with col131:
            communication = st.selectbox('연락 수단을 선택하세요', ['휴대전화 번호', '인스타그램 ID', '카카오톡 ID'])
        with col132:
            with st.container():
                st.markdown(
                    f'<div style="height: 72px; line-height: 62px; background-color:#C8EFF2 ; font-family: Malgun Gothic; white-space: pre-wrap; overflow-wrap: break-word; padding: 0 1.0rem; border: 1px solid #f0f2f6; border-radius:5px;">{"연락처 입력"}</div>',
                    unsafe_allow_html=True,
                )
        with col133:
            number = st.text_input("전화번호의 경우, '010-1234-1234' 형식으로 입력하세요")


        st.markdown("#### 상담 유형")

        col40, col41, col42, col43, col44, col45 = st.columns(6)  # col 나누기
        with col40:  # col 나누기
            st.markdown(
                f'<div style="height: 60px; line-height: 50px; background-color:#C8EFF2 ; font-family: Malgun Gothic; white-space: pre-wrap; overflow-wrap: break-word; padding: 0 1.0rem; border: 1px solid #f0f2f6; border-radius:5px;">{"상담 유형"}</div>',
                unsafe_allow_html=True,
            )
        with col41:
            grade = st.checkbox("학업/진로")
            relationship = st.checkbox("대인관계")
        with col42:
            sex = st.checkbox("성")
            bullying = st.checkbox("학교폭력")
        with col43:
            domestic_violence = st.checkbox("가정폭력")
            depression = st.checkbox("우울증")
        with col44:
            lifestyle = st.checkbox("생활습관")
            addiction = st.checkbox("컴퓨터 중독")
        with col45: 
            drugs = st.checkbox("마약")

        st.markdown("#### 원하는 상담사 유형")

        col50, col51, col52, col53 = st.columns(4)  # col 나누기
        with col50:
            st.markdown(
                f'<div style="height: 50px; line-height: 40px; background-color:#C8EFF2 ; font-family: Malgun Gothic; white-space: pre-wrap; overflow-wrap: break-word; padding: 0 1.0rem; border: 1px solid #f0f2f6; border-radius:5px;">{"상담사 유형"}</div><br>',
                    unsafe_allow_html=True,
                )
        with col51:  
            Teenager_counsler = st.checkbox("또래 상담사")
        with col52:
            College_counsler = st.checkbox("대학생 상담사")
        with col53:
            Adult_counsler = st.checkbox("전문 상담사")

        with st.form(key='tab1_first'):
            add_text = st.text_input("추가적으로 원하는 상담 내용을 입력하세요")


            # 상담 내역을 저장하는 버튼
            if st.form_submit_button(label='상담 예약 요청'):

                new_data = {
                    "start_date": [start_date],
                    "start_hour": [start_hour],
                    "start_minute": [start_minute],
                    "name": [name],
                    "age": [age],
                    "gender": [gender],
                    "communication": [communication],
                    "number": [number],
                    "grade": [grade],
                    "relationship": [relationship],
                    "sex": [sex],
                    "bullying": [bullying],
                    "domestic_violence": [domestic_violence],
                    "depression": [depression],
                    "lifestyle": [lifestyle],
                    "addiction": [addiction],
                    "drugs": [drugs],
                    "Teenager_counsler": [Teenager_counsler],
                    "College_counsler": [College_counsler],
                    "Adult_counsler": [Adult_counsler],
                    "additional_text": [add_text],
                    "status": ["requested"]
                }

                new_df = pd.DataFrame(new_data)
                df = df.append(new_df, ignore_index=True)
                df.to_csv("상담 학생 데이터.csv", index=False, encoding='utf-8-sig')

with tab2:
    st.markdown('## 상담사 정보 입력')

    if os.path.exists("상담사 리스트.csv"):
        agent_list_df = pd.read_csv("상담사 리스트.csv")

    with st.form(key='tab2_form'):
        agent_name = st.text_input("상담사 이름을 입력하세요")
        agent_contact = st.text_input("전화번호를 '010-1234-1234' 형식으로 입력하세요", value="", type="default")
        agent_position = st.selectbox("상담사 직책을 선택하세요", ['또래 상담사', '대학생 상담사', '전문 상담사'])

        if st.form_submit_button(label='상담사 정보 저장'):
            agent_data = {
                "이름": [agent_name],
                "연락처": [str(agent_contact)],
                "직책": [agent_position],
                "appointment_times": [[]]
            }

            new_agent_df = pd.DataFrame(agent_data)

            if os.path.exists("상담사 리스트.csv"):
                agent_list_df = agent_list_df.append(new_agent_df, ignore_index=True)
            else:
                agent_list_df = new_agent_df

            agent_list_df.to_csv("상담사 리스트.csv", index=False, encoding='utf-8-sig')
            st.success("상담사 정보가 저장되었습니다.")

    st.markdown("#### 상담사 데이터 삭제")
    delete_agent_index = st.number_input("삭제할 상담사 데이터 인덱스를 입력하세요 (0부터 시작)", min_value=0, step=1, key='delete_agent_index')

    if st.button("상담사 데이터 삭제"):
        if 0 <= delete_agent_index < len(agent_list_df):
            agent_list_df = agent_list_df.drop(delete_agent_index).reset_index(drop=True)
            agent_list_df.to_csv("상담사 리스트.csv", index=False, encoding='utf-8-sig')
            st.success(f"인덱스 {delete_agent_index}의 상담사 데이터가 삭제되었습니다.")
        else:
            st.warning("유효한 상담사 데이터를 입력하세요.")

    st.markdown("### 저장된 상담사 정보")
    if os.path.exists("상담사 리스트.csv"):
        agent_list_df = pd.read_csv("상담사 리스트.csv")
        agent_list_df["연락처"] = agent_list_df["연락처"].astype(str)
        st.write(agent_list_df)
    else:
        st.warning("아직 상담사 정보가 없습니다.")

with tab3:
    st.markdown("## 상담 스케줄 관리 및 상담사 배정")

    if os.path.exists("상담 학생 데이터.csv"):
        consultation_student_df = pd.read_csv("상담 학생 데이터.csv")

        # 상담 학생 데이터에서 원하는 상담사 유형 열 생성
        consultation_student_df.loc[consultation_student_df['Teenager_counsler'], '원하는 상담사 유형'] = '또래 상담사'
        consultation_student_df.loc[consultation_student_df['College_counsler'], '원하는 상담사 유형'] = '대학생 상담사'
        consultation_student_df.loc[consultation_student_df['Adult_counsler'], '원하는 상담사 유형'] = '전문 상담사'

        # 상담 현황을 표로 표시
        st.markdown("### 상담 현황")
        columns_to_display = ['start_date', 'name', 'number', 'status', '원하는 상담사 유형']
        st.write(consultation_student_df[columns_to_display])

        # 이후 작업을 진행할 수 있습니다.
    else:
        st.warning("아직 상담 학생 데이터가 없습니다.")

    if os.path.exists("상담사 리스트.csv"):
        agent_list_df = pd.read_csv("상담사 리스트.csv")

        st.markdown("### 상담사 배정")

        consultation_index = st.number_input("상담 학생 순번을 입력하세요 (0부터 시작)", min_value=0, step=1)

        if 0 <= consultation_index < len(consultation_student_df):
            preferred_counselor_type = consultation_student_df.loc[consultation_index, '원하는 상담사 유형']
            available_counselors = agent_list_df[agent_list_df['직책'] == preferred_counselor_type]

            st.markdown(f"### {preferred_counselor_type} 상담사 목록")
            st.write(available_counselors)
        else:
            st.warning("유효한 순번을 입력하세요.")

    if os.path.exists("상담사 리스트.csv") and os.path.exists("상담 학생 데이터.csv"):
        st.markdown("### 상담사 선택 및 배정")

        counselor_index = st.number_input("상담사 리스트에서 상담사 순번을 입력하세요 (0부터 시작)", min_value=0, step=1)

        if 0 <= counselor_index < len(agent_list_df):
            chosen_counselor = agent_list_df.loc[counselor_index, '이름']
            st.write(f"선택된 상담사: {chosen_counselor}")

            assign_button = st.button("상담사 배정")

            if assign_button:
                consultation_student_df.loc[consultation_index, '상담사'] = chosen_counselor
                consultation_student_df.loc[consultation_index, 'status'] = "배정 완료"
                consultation_student_df.to_csv("상담 학생 데이터.csv", index=False, encoding='utf-8-sig')
                st.success("상담사가 배정되었습니다.")
        else:
            st.warning("유효한 상담사 순번을 입력하세요.")

    st.markdown("### 상담 취소")
    cancel_index = st.number_input("취소할 상담 학생 번호를 입력하세요 (0부터 시작)", min_value=0, step=1, key='cancel_index')

    if st.button("상담 취소"):
        if 0 <= cancel_index < len(consultation_student_df):
            consultation_student_df.loc[cancel_index, 'status'] = 'cancelled'
            consultation_student_df.to_csv("상담 학생 데이터.csv", index=False, encoding='utf-8-sig')
            st.success(f"{cancel_index}의 상담이 취소되었습니다.")
        else:
            st.warning("유효한 번호를 입력하세요.")

    st.markdown("#### 상담 학생 데이터 삭제")
    delete_student_index = st.number_input("삭제할 상담 학생 데이터 인덱스를 입력하세요 (0부터 시작)", min_value=0, step=1, key='delete_student_index')

    if st.button("상담 학생 데이터 삭제"):
        if 0 <= delete_student_index < len(consultation_student_df):
            consultation_student_df = consultation_student_df.drop(delete_student_index).reset_index(drop=True)
            consultation_student_df.to_csv("상담 학생 데이터.csv", index=False, encoding='utf-8-sig')
            st.success(f"{delete_student_index}번 상담 학생 데이터가 삭제되었습니다.")
        else:
            st.warning("유효한 학생 데이터를 입력하세요.")
