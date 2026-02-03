import pandas as pd
df_b = pd.read_csv("data/site_b_readings.csv", parse_dates = ['timestamp'], index_col = 'timestamp')
print("Site B moisture stats:")
print(df_b['moisture_pct'].describe())
print("High-flow (>3 LPM) incidents:")
high_flow_b = df_b[df_b['flow_rate_lpm'] > 3.0]
print(high_flow_b[['device_id', 'flow_rate_lpm']])


common_time = "2025-04-01 00:00:00"

a_at_time = df_a.loc