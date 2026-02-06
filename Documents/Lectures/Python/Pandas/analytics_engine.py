import pandas as pd
import numpy as np
import json
from scipy.stats import zscore
from pprint import pprint

#Load data
df = pd.read_csv("data/sensor_logs_zone_demo.csv", parse_dates=['timestamp'], index_col=['timestamp'])
print(f"Loaded {len(df)} sensor logs with {df['device_id'].nunique()} devices.")

# Sample working functions

def compute_device_stats(df, device_id):
    # Return dict of stats for a single device
    df = df[df['device_id'] == device_id]
    device_stats = {
        "device_id": device_id,
        "records": len(df),
        "avg_moisture": df['moisture_level'].mean(),
        "min_moisture": df['moisture_level'].min(),
        "max_moisture": df['moisture_level'].max(),
        "avg_temperature": df['temperature'].mean(),
        "min_temperature": df['temperature'].min(),
        "max_temperature": df['temperature'].max(),
        "avg_signal_strength": df['signal_strength'].mean(),
        "min_signal_strength": df['signal_strength'].min(),
        "max_signal_strength": df['signal_strength'].max(),
        "zones": df['zone'].unique(),
        "avg_battery_level": df['battery_level'].mean(),
        "min_battery_level": df['battery_level'].min(),
        "max_battery_level": df['battery_level'].max(),
    }
    return device_stats

def get_anomalous_readings(device_series, threshold = 3):
    # Use z-score to identify outliers
    device_series["moisture_z"] = (
    (device_series['moisture_level'] - device_series['moisture_level'].mean()) / device_series['moisture_level'].std()
    )
    device_series['anomalies'] = abs(device_series['moisture_z']) > 3
    return device_series

def analyze_by_zone(df, min_risk_percent = 30):
    # Use boolean indexing to find high-risk zones
    df['min_risk'] = df[df['moisture'] < min_risk_percent]
    df['high_risk'] = df[df['moisture'] > min_risk_percent]
    return df
def analyze_signal_health(df, min_risk_percent = 30):
    # Boolean indexing for signal health
    pass

anomalies = get_anomalous_readings(df, 3)

print(anomalies.head())