#importing required libraries

import streamlit as st
from datetime import time
from datetime import datetime
import pandas as pd
import psycopg2


conn = psycopg2.connect("dbname='test_db' user='root' host='pg_container' password='root'") 

cur = conn.cursor()

insert_query = """
INSERT INTO streamlit_test1 (
country,
fund,
portfolio,
people_quality_score,
people_quality_comment,
cyber_security_score,
cyber_security_comment,
time_stamp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""



#adding a simple slider

country_choice = st.sidebar.selectbox("Country: ", ("India", "Pakistan","Afganistan","United States Of America"))
fund_choice = st.sidebar.selectbox("Fund: ", ("Random1", "Random_2","Random_3","Random_4"))
portfolio_choice = st.sidebar.selectbox("Porfolio: ", ("Portfolio_1", "Portfolio_2"))

with st.form('People-Quality'):
    if "disabled" not in st.session_state:
        st.session_state["disabled"] = False
    People_Quality = st.slider('People and Quality', 0, 5, 1)
    people_quality_comment = st.text_input("Comment")
    submit_no = st.form_submit_button(label='Submit')

st.write(f"Score Submitted: {People_Quality}")
st.write(people_quality_comment)


#adding a simple slider

with st.form('cyber-security'):
    cyber_security = st.slider('Cyber Security', 0, 5, 1)
    cyber_security_comment = st.text_input("Comment")
    submit = st.form_submit_button(label='Submit')

if submit:
    st.write(f"Score Submitted: {cyber_security}")
    cur.execute(insert_query,(country_choice,fund_choice,portfolio_choice,People_Quality,people_quality_comment,cyber_security,cyber_security_comment, datetime.now()))
    conn.commit()
    cur.close()


