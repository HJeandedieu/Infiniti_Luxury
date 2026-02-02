import pandas as pd
import os

# print("Files in data/ :", os.listdir("data/"))
#
# df_a = pd.read_csv("data/site_a_readings.csv")
# print("First 5 rows:")
# print(df_a.head())
#
# print(df_a.dtypes)

df_a = pd.read_csv("data/site_a_readings.csv", parse_dates=["timestamp"], index_col = "timestamp")
print(df_a.head())
print("Data types:")
print(df_a.dtypes)
print("Index types:")
print(df_a.index)

print("Shape(rows, columns):", df_a.shape)
print("Columns:", df_a.columns)
print("Index range (head):")
print(df_a.index.min(), "to", df_a.index.max())

print("---Summary statistics for numeric columns ---")
print(df_a.describe())


moisture_a = df_a['moisture_pct']
print("Moisture pct (first 10):")
print(moisture_a.head(10))

sensors = df_a[['moisture_pct', 'flow_rate_lpm']]
print("selected sensors (head):")
print(sensors.head())

high_fluid =