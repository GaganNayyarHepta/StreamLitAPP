#importing required libraries

import streamlit as st
from datetime import time
from datetime import datetime
import pandas as pd
import psycopg2
from PIL import Image

image_path = 'BPEA-EQT-logo_.png'
def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

my_logo = add_logo(logo_path=image_path, width=60, height=60)
st.image(my_logo)
st.title("PMC ASSESSMENT")

conn = psycopg2.connect("dbname='postgres' user='root' host='pg_container' password='root'") 

cur = conn.cursor()

insert_query = """
INSERT INTO user_input (
	country,
	fund,
	portfolio,
	company_performance,
	company_performance_comment,
	company_stronger,
	company_stronger_comment,
	gap_status,
	gap_status_comment,
	relative_peer,
	relative_peer_comment,
	time_stamp) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""



#adding a simple slider

country_choice = st.sidebar.selectbox("Country: ", ("India", "Pakistan","Afganistan","United States Of America"))
fund_choice = st.sidebar.selectbox("Fund: ", ("Random1", "Random_2","Random_3","Random_4"))
portfolio_choice = st.sidebar.selectbox("Porfolio: ", ("Portfolio_1", "Portfolio_2"))

Overall, Gap =  st.tabs(['Overall', 'Gap'])
with Overall.form('Company-Performance'):
        
    company_performance = st.slider('Is the company performance improving', 0, 5, 1)
    company_performance_comment = st.text_input("Comment")
    submit_no = st.form_submit_button(label='Submit')
    st.write(f"Score Submitted: {company_performance}")
    st.write(company_performance_comment)

with Overall.form('Company-Stronger'):
        
    company_stronger = st.slider('Is the company getting stronger', 0, 5, 1)
    company_stronger_comment = st.text_input("Comment")
    submit_no = st.form_submit_button(label='Submit')
    st.write(f"Score Submitted: {company_stronger}")
    st.write(company_stronger_comment)

with Gap.form('Gap'):
        
    gap_status = st.slider('Is the gap getting smaller or larger', 0, 5, 1)
    gap_status_comment = st.text_input("Comment")
    submit_no = st.form_submit_button(label='Submit')
    st.write(f"Score Submitted: {gap_status}")
    st.write(gap_status_comment)

with Gap.form('Relative-Peers'):
        
    relative_peer = st.slider('Is the company getting stronger', 0, 5, 1)
    relative_peer_comment = st.text_input("Comment")
    submit_all = st.form_submit_button(label='Submit')
    st.write(f"Score Submitted: {relative_peer}")
    st.write(relative_peer_comment) 

if submit_all:
    st.write(f"Score Submitted: {relative_peer}")
    cur.execute(insert_query,(country_choice,fund_choice,portfolio_choice,company_performance,company_performance_comment,company_stronger,company_stronger_comment, gap_status,gap_status_comment,relative_peer,relative_peer_comment,datetime.now()))
    conn.commit()
    cur.close()


