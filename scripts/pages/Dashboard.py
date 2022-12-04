import plotly.express as px
import streamlit as st
from datetime import time
from datetime import datetime
import pandas as pd
import psycopg2
import plotly.graph_objects as go
import plotly.io as pio

conn = psycopg2.connect("dbname='test_db' user='root' host='pg_container' password='root'") 

cur = conn.cursor()

fetch_query = """select * from streamlit_test1"""

cur.execute(fetch_query)
columns = cur.description
data = cur.fetchall()


columns_name = [item[0] for item in columns]
df = pd.DataFrame(data=data, columns=columns_name)


country_choice = st.sidebar.selectbox("Country: ", ("India", "Pakistan","Afganistan","United States Of America"))
fund_choice = st.sidebar.selectbox("Fund: ", ("Random1", "Random_2","Random_3","Random_4"))
portfolio_choice = st.sidebar.selectbox("Porfolio: ", ("Portfolio_1", "Portfolio_2"))


df = df[(df['country'] == country_choice) & (df['fund'] == fund_choice)]
df = df[(df['portfolio'] == portfolio_choice)]
st.write(df)



line_people_quality = go.Figure()

line_people_quality.add_trace(go.Scatter(x=list(df['time_stamp']), y=list(df['people_quality_score']),mode='lines+markers',text='people_quality_score',
    line=dict(width=2,dash='dot')))
line_people_quality.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
line_people_quality.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False),paper_bgcolor="rgb(0,0,0,0)",template='plotly_dark',title='People Quality')
line_people_quality.update_layout(
    autosize=False,
    width=600,
    height=400,)


line_cyber_security = go.Figure()

line_cyber_security.add_trace(go.Scatter(x=list(df['time_stamp']), y=list(df['cyber_security_score']),mode='lines+markers',text='cyber_security_score',
    line=dict(width=2,dash='dot')))
line_cyber_security.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
line_cyber_security.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False),paper_bgcolor="rgb(0,0,0,0)",template='plotly_dark',title='Cyber Security')
line_cyber_security.update_layout(
    autosize=False,
    width=600,
    height=400,)

linegraph1, linegraph2 = st.columns([1,1])

with linegraph1:
    st.plotly_chart(line_people_quality)

with linegraph2:
    st.plotly_chart(line_cyber_security)

