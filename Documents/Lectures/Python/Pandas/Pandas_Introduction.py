import pandas as pd
import os

df_a = pd.read_csv("data/site_a_readings.csv", parse_dates=['timestamp'], index_col = 'timestamp')
# print("New DataFrame structure:")
# print(df_a.head())
# print("Data types:")
# print(df_a.dtypes)
# print("Index types")
# print(df_a.index)

# print("Shape (row, columns):", df_a.shape)
# print("Columns:", df_a.columns)
# print("Index range (head):")
# print(df_a.index.min(), "to", df_a.index.max())
#
# print("----Summary statistics for numeric columns----")
# print(df_a.describe())

moisture_a = df_a['moisture_pct']
print("Moisture pct (first 10):")
print(moisture_a.head(10))

sensors = df_a[['moisture_pct', "flow_rate_lpm"]]
print("Selected sensors (head):")
print(sensors.head())

# FILTERING DATA USING CONDITIONS

high_fluid = df_a[df_a["moisture_pct"] > 50]
print("High moisture (>50%) events:")
print(high_fluid[['device_id', 'moisture_pct', 'flow_rate_lpm']])

#Combine filters: high water and flow possible

risky = df_a[(df_a['moisture_pct'] > 50) & (df_a['flow_rate_lpm'] > 1.5)]
print("High-risk Alerts (>50% + > 1.5 LPM):")
print(risky)


df_b = pd.read_csv("data/site_b_readings.csv", parse_dates = ['timestamp'], index_col = 'timestamp')
print("Site B moisture stats:")
print(df_b['moisture_pct'].describe())
print("High-flow (>3 LPM) incidents:")
high_flow_b = df_b[df_b['flow_rate_lpm'] > 3.0]
print(high_flow_b[['device_id', 'flow_rate_lpm']])


common_time = "2025-04-01 00:00:00"

a_at_time = df_a.loc[[common_time]]

b_at_time = df_a.loc[[common_time]]

print(f"Site A at {common_time}:")
print(a_at_time[['device_id','moisture_pct', 'flow_rate_lpm']])
print(f"Site B at {common_time}:")
print(b_at_time[['device_id','moisture_pct', 'flow_rate_lpm']])

df_total = pd.concat([df_a, df_b])
# print(df_total['moisture_pct'].mean())
#
# df_total = df_total.sort_index()
#
# df_total['moisture_change'] = df_total['moisture_pct'].diff()
#
# filtered = df_total[df_total['moisture_change'] > 3]
# print(filtered.head())
#
# df_a.to_csv("data/site_a_tidy.csv")

print("Mean moisture per device")
print(df_total.groupby("device_id")['moisture_pct'].mean())
