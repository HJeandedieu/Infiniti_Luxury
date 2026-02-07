import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

#Load sensor data with automatic time parsing
df = pd.read_csv("data/sensor_data_hourly.csv", parse_dates = ['timestamp'])


#Set timestamp as index for time-series operations
df = df.set_index('timestamp')

#Sort by time to ensure chronological order

df = df.sort_index()

print("First 5 rows:")
print(df.head())

print("Index info:")
print(df.index.dtype)

#Filtering for one Sensor

sensor = df[df['device_id']== 'S01'].copy()
print(f"Sensor S01 has {len(sensor)} hourly readings")

sensor['flow_rate'] = pd.to_numeric(sensor['flow_rate'], errors = 'coerce')
#RESAMPLE TO DAILY AVERAGES FOR EACH COLUMN

daily = sensor[['moisture','temperature','flow_rate']].resample("D").mean()
print("Dail averages for S01:")
print(daily.head(7))

#check the index

print("Daily index (days only):")
print(daily.index)


# VISUALIZATION PLOT

plt.figure(figsize = (10,5))
plt.plot(daily.index, daily['moisture'], marker ='o', label ='moisture', color = "green")
plt.title("Daily Average Moisture (Resampled) - S01")
plt.xlabel("Date")
plt.ylabel("Moisture(%)")
plt.xticks(rotation = 45)
plt.legend()
plt.tight_layout()
plt.show()

#Detecting trends using rolling averages

#calculate 7-day rolling average (centered window)

daily['moisture_roll7'] = daily['moisture'].rolling(window = 7, center=True).mean()

daily['temp_roll7'] = daily['moisture'].rolling(window = 7, center=True, min_periods = 3).mean()

print("With rolling averages:")
print(daily[['moisture', 'moisture_roll7', 'temperature', "temp_roll7"]].tail(10))

#compute day-over-day moisture change
daily['delta_moisture'] = daily['moisture'].diff()

#Mark days with drop > 3%

daily['draining_event'] = daily['delta_moisture'] < -3

#Mark irrigation days (big increase)

daily['irrigation_detected'] = daily['delta_moisture'] > 4

print("Key days (last 5) :")
with pd.option_context("display.max_columns", None):
    print(daily[['moisture', 'delta_moisture','draining_event', 'irrigation_detected' ]].tail())

#Count total
n_watering = daily['irrigation_detected'].sum()
n_drying = daily['draining_event'].sum()
print(f"Detected {n_watering} watering and {n_drying} draining events")

#SUMMARY REPORT

summary = daily[[
    'device_id', 'moisture', 'temperature', 'flow_rate',
    'moisture_roll7', 'draining_event', 'irrigation_detected',
]].dropna(subset=['moisture'])

#Reset index to include date in csv
summary_with_data = summary.reset_index()

#save
summary_with_data.to_csv("summarized_daily_sensor_S01.csv", index = False)
print("Summary saved to 'summarized_daily_sensor_S01.csv'")