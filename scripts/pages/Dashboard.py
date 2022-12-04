import plotly.express as px
import streamlit as st
from datetime import time
from datetime import datetime
import pandas as pd
import psycopg2
import plotly.graph_objects as go
import plotly.io as pio

conn = psycopg2.connect("dbname='postgres' user='root' host='pg_container' password='root'") 

cur = conn.cursor()

fetch_query = """select * from user_input;"""

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

def line_graph(x_axis,y_axis,text,title):
    line_chart = go.Figure()
    line_chart.add_trace(go.Scatter(x=list(x_axis), y=list(y_axis),mode='lines+markers',text=text))
    line_chart.update_traces(line=dict(shape='spline',color='white',width=3,dash='dot'),marker=dict(size=10))
    line_chart.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
    line_chart.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False),paper_bgcolor="rgb(0,0,0,0)",template=None,title=title)
    line_chart.update_layout(
        autosize=False,
        width=800,
        height=500)
    
    return line_chart

overall_company_performance = line_graph(df['time_stamp'], df['company_performance'], text=df['company_performance_comment'], title= 'Overall: Company Performance')

overall_company_stronger = line_graph(df['time_stamp'], df['company_stronger'], text=df['company_stronger_comment'], title= 'Overall: Company Stronger')

linegraph1, linegraph2 = st.columns([1,1])

with linegraph1:
    st.plotly_chart(overall_company_performance)

with linegraph2:
    st.plotly_chart(overall_company_stronger)

gap_gap_status = line_graph(df['time_stamp'], df['gap_status'], text=df['gap_status_comment'], title= 'GAP: Gap Status')

gap_relative_peer = line_graph(df['time_stamp'], df['relative_peer'], text=df['relative_peer_comment'], title= 'GAP: Relative Peer')

linegraph3, linegraph4 = st.columns([1,1])

with linegraph3:
    st.plotly_chart(gap_gap_status)

with linegraph4:
    st.plotly_chart(gap_relative_peer)