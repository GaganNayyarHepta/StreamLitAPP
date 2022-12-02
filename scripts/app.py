#importing required libraries

import streamlit as st

from datetime import time

from datetime import datetime
#import psycopg2

#conn = psycopg2.connect("dbname='test_db' user='root' host='localhost' password='root'") 

#cur = conn.cursor()

insert_query = """
INSERT INTO streamlit_test1 (people_quality_score,
people_quality_comment,
cyber_security_score,
cyber_security_comment) VALUES (%s,%s,%s,%s)
"""



#adding a simple slider

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
"""
if submit:
    st.write(f"Score Submitted: {cyber_security}")
    cur.execute(insert_query,(People_Quality,people_quality_comment,cyber_security,cyber_security_comment))
    conn.commit()
    cur.close()"""