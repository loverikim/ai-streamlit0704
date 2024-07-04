import streamlit as st
import national_pension as np

# 사이드바 화면
st.sidebar.header("로그인")
user_id = st.sidebar.text_input('아이디(ID) 입력', value="streamlit", max_chars=15)
user_password = st.sidebar.text_input('패스워드(Password) 입력', value="", type="password")

if user_password == '1234':

    st.sidebar.header("포트폴리오")
    selectbox_options = ["",'탐색적데이터분석','머신러닝_예측'] # 셀렉트 박스의 선택 항목
    your_option = st.sidebar.selectbox('메뉴?', selectbox_options, index=0) # 셀렉트박스의 항목 선택 결과
    st.sidebar.write('**당신의 선택**:', your_option)

    # 메인(Main) 화면
    st.subheader(your_option, divider='rainbow')
    
    if your_option == "탐색적데이터분석":
        st.write("탐색적데이터분석")   
        np.np_main()
    elif your_option == "머신러닝_예측":
        st.write("머신러닝_예측")
    else:
        st.write("환영합니다.")