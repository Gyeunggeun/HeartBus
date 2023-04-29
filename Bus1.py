import pandas as pd
import streamlit as st
import numpy as np
import datetime
import os


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
tab1, tab2 = st.tabs(['상담 예약 페이지', '대시보드'])
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
            number = st.text_input("연락처를 입력하세요")


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
            Teenager_counsler = st.checkbox("청소년 상담사")
        with col52:
            College_counsler = st.checkbox("대학생 상담사")
        with col53:
            Adult_counsler = st.checkbox("성인 상담사")

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
    st.markdown('## 대시보드')
    st.info('금일 상담 학생 정보')

    agent_list_df = pd.read_csv("상담사 리스트.csv")
    consultation_student_df = pd.read_csv("상담 학생 데이터.csv")
    consultation_student_df['start_date'] = pd.to_datetime(consultation_student_df['start_date']).dt.date

    today = datetime.date.today()

    # 오늘의 학생 확인
    todays_appointments_df = consultation_student_df[consultation_student_df['start_date'] == today]
    todays_appointments_df['start_time'] = pd.to_datetime(todays_appointments_df['start_date'].astype(str) + ' ' +
                                                          todays_appointments_df['start_hour'].astype(str) + ':' +
                                                          todays_appointments_df['start_minute'].astype(str),
                                                          format='%Y-%m-%d %H:%M')

    # 예약 내용 업데이트
    agent_list_df["appointment_times"] = agent_list_df["이름"].apply(
        lambda x: todays_appointments_df[todays_appointments_df["name"] == x]["start_time"].tolist())

    # 업데이트된 내용 csv 파일에 저장
    agent_list_df.to_csv("상담사 리스트.csv", index=False, encoding='utf-8-sig')

    # 상담사 리스트와 예약 시간 표시
    st.markdown("### 금일 상담사 정보")
    st.write(agent_list_df)

    # 예약시간 중복 확인
    def check_overlap(appointments, agent, start_time):
        agent_appointments = appointments[appointments["name"] == agent]
        for _, appointment in agent_appointments.iterrows():
            if appointment["start_time"] == start_time:
                return True
        return False

    # 예약 시간이 중복되었다면, 중복
    with st.form(key="tab2_appointment"):
        agent = st.selectbox("상담사를 선택하세요", agent_list_df["이름"].unique())
        start_time = st.time_input("상담 시간을 선택하세요")

        if st.form_submit_button("예약 시간 확인"):
            overlap = check_overlap(todays_appointments_df, agent, start_time)
            if overlap:
                st.warning("해당 시간은 예약이 불가능합니다.")
            else:
                st.success("해당 시간은 예약이 가능합니다.")

    # 상담 승인 버튼
    if st.button("상담 승인"):
        selected_row_index = st.number_input("승인할 상담의 행 번호를 입력하세요", min_value=0, step=1)
        consultation_student_df.loc[selected_row_index, 'status'] = 'approved'
        consultation_student_df.to_csv("상담 학생 데이터.csv", index=False, encoding='utf-8-sig')
        st.success("상담이 승인되었습니다.")

    st.markdown("### 금일 상담 학생 정보")
    st.write(todays_appointments_df)
