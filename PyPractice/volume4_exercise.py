import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float

# loading 2 csv files into 2 dataframes
df1 = pd.read_csv('/Users/amakki/Documents/Coding/IDLE-App-folder/volume4_case_study/enterprise-survey-2023-financial-year-provisional.csv')
df2 = pd.read_csv('/Users/amakki/Documents/Coding/IDLE-App-folder/volume4_case_study/survey-2022-business-finance.csv', encoding='latin1')
# create a SQLite database engine
engine = create_engine('sqlite:///business_survey.db')
# define table schema
class EnterpriseSurvey:
    __tablename__ = 'enterprise_survey'
    id = Column(Integer, primary_key=True)
    Year = Column(Integer)
    Industry_aggregation_NZSIOC = Column(String)
    Industry_code_NZSIOC = Column(Integer)
    Industry_name_NZSIOC = Column(String)
    Units = Column(String)
    Variable_code = Column(String)
    Variable_name = Column(String)
    Variable_category = Column(String)
    Value = Column(Integer)
    Industry_code_ANZSIC06 = Column(String)
class BusinessFinanceSurvey:
    __tablename__ = 'business_finance_survey'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    industry = Column(String)
    level = Column(Integer)
    size = Column(String)
    line_code = Column(String)
    value = Column(Integer)
# write DataFrames to SQL tables
df1.to_sql('enterprise_survey', engine, if_exists='replace', index=False)
df2.to_sql('business_finance_survey', engine, if_exists='replace', index=False)

print(df1.head())
print(df2.head())
print("DataFrames have been written to the SQLite database with the specified schemas")
conn = sqlite3.connect('business_survey.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(tables)
conn.close()

data_array1 = df1.to_numpy()
data_array2 = df2.to_numpy()
print(data_array1.shape)
print(data_array2.shape)



