#!/usr/bin/env python
# coding: utf-8

# In[11]:


import sqlite3
import pandas as pd


csv_file_path = '/Users/mac/Desktop/DoneDeal WebScraping/DoneDealCars.csv'
df = pd.read_csv(csv_file_path)

#Connecting to an in-memory SQLite database
conn = sqlite3.connect(':memory:')

#Save the DataFrame into the SQLite database
df.to_sql('csv_data', conn, index=False)

#Execute SQL queries on the data
query = "SELECT Title FROM csv_data where Carbrand = 'Mazda';"
result_df = pd.read_sql_query(query, conn)

#Close the connection 
conn.close()

print(result_df)


# In[ ]:




