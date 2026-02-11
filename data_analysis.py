import pandas as pd
import mysql.connector
from config import db_config
import matplotlib.pyplot as plt

conn = mysql.connector.connect(**db_config)
query = "SELECT * FROM earthquakes"
df = pd.read_sql(query, conn)
conn.close()

print("📊 Mean Depth:", df['depth'].mean())
print("📊 Max Magnitude:", df['magnitude'].max())
print("📊 Min Magnitude:", df['magnitude'].min())

df['year'] = pd.to_datetime(df['date']).dt.year
yearly = df.groupby('year').size()
print("\n📅 Earthquakes per Year:\n", yearly)

bins = [0, 70, 300, 700]
labels = ['Shallow', 'Intermediate', 'Deep']
df['depth_range'] = pd.cut(df['depth'], bins=bins, labels=labels)
print("\n🌎 Earthquakes by Depth Range:\n", df['depth_range'].value_counts())


print("\n🌋 Top 5 Deepest Earthquakes:\n", df.sort_values(by='depth', ascending=False).head())

print("\n💥 Top 5 Most Powerful Earthquakes:\n", df.sort_values(by='magnitude', ascending=False).head())

yearly.plot(kind='bar', figsize=(12,6), title='Earthquakes per Year', color='skyblue')
plt.xlabel('Year')
plt.ylabel('Number of Earthquakes')
plt.tight_layout()
plt.show()

df['depth'].plot(kind='hist', bins=30, title='Depth Distribution of Earthquakes', color='orange')
plt.xlabel('Depth (km)')
plt.tight_layout()
plt.show()
