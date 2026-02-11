import pandas as pd
import mysql.connector
from config import db_config

df = pd.read_csv('database.csv')

print("CSV Columns:", df.columns)

df = df[['Date', 'Latitude', 'Longitude', 'Depth', 'Magnitude']].dropna()
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna()

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS earthquakes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE,
        latitude FLOAT,
        longitude FLOAT,
        depth FLOAT,
        magnitude FLOAT
    )
""")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO earthquakes (date, latitude, longitude, depth, magnitude)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        row['Date'].date(),
        row['Latitude'],
        row['Longitude'],
        row['Depth'],
        row['Magnitude']
    ))

conn.commit()
cursor.close()
conn.close()
print("Data inserted into MySQL successfully.")
