import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('database.db')

# Read CSV files and write to SQLite tables
precautions_df = pd.read_csv('/home/fizzi/Documents/SYMPRI/database/datasets/precautions(1).csv',index_col=0)
medications_df = pd.read_csv('/home/fizzi/Documents/SYMPRI/database/datasets/medications(1).csv', index_col=0)
symptoms_df = pd.read_csv('/home/fizzi/Documents/SYMPRI/database/datasets/symptoms(1).csv', index_col=0)

precautions_df.to_sql('precautions', conn, if_exists='replace', index=False)
medications_df.to_sql('medications', conn, if_exists='replace', index=False)
symptoms_df.to_sql('symptoms', conn, if_exists='replace', index=False)

conn.close()
