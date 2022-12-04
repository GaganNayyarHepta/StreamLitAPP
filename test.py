
from datetime import time
from datetime import datetime
import pandas as pd
import psycopg2



conn = psycopg2.connect("dbname='test_db' user='root' host='localhost' password='root'") 

cur = conn.cursor()

fetch_query = """select * from streamlit_test1"""

cur.execute(fetch_query)
columns = cur.description
data = cur.fetchall()


columns_name = [item[0] for item in columns]
df = pd.DataFrame(data=data, columns=columns_name)
print(df)