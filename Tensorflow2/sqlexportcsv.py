# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:20:11 2021

@author: 11004142
"""

import pymysql
import pandas as pd



class MySQLConnector:
    def __init__(self):
        self.host = '10.41.241.230'
        self.port = 30123
        self.user = 'OneAI_App'
        self.password = 'yoyoeat2020'
        self.database = 'OPS_WIH'
        self.charset = 'utf8'
        self.query = None

    def set_sql_query(self, query):
        self.query = query
        # print("Setting SQL Query:\n", self.query)

    def get_data(self):
        conn = pymysql.connect(
            host = self.host, 
            port = self.port,
            user = self.user, 
            password = self.password, 
            database = self.database,
            charset = self.charset, 
            cursorclass = pymysql.cursors.SSDictCursor) # it is neccesary to have this class for convert to DataFrame.
        cursor = conn.cursor()
        cursor.execute(self.query)
        groups = cursor.fetchall()
        cursor.close()
        return groups
    


# sql = '''SELECT  image_name, model_name, source, label, ai_answer, ai_score, workday
#          FROM OPS_WIH.report_daily_online_report
#          WHERE source  ='GRR_daily' 
#          AND workday BETWEEN '2021-03-01' AND '2021-05-31';''' 
 
sql = '''SELECT  image_name, model_name, kb_model, location, sn, import_time
          FROM OPS_WIH.report_daily_online_report
          WHERE import_time BETWEEN '2021-03-01' AND '2021-06-30';''' 
 

x = MySQLConnector()
x.set_sql_query(sql)
data = x.get_data()
# print(type(data))

# df = pd.DataFrame(data)
df2 = pd.DataFrame(data)

# df3 = df.merge(df2, how='inner', on='image_name')






df2.to_csv(r'C:\Users\11004142\Desktop\wih.csv',index = False, header=True)











