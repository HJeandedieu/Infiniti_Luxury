import pandas as pd
import numpy as np
import json
from scipy.stats import zscore
from pprint import pprint

#Load data
df = pd.read_csv("data/sensor_logs_zone_demo.csv", parse_dates=['timestamp'], index_col=['timestamp'])
print(f"Loaded {len(df)} sensor logs with {df['device_id'].nunique()} devices.")

# Sample working functions

devices = df['device_id'].unique()

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

def per_device_stats(df):
    device_stats = df.groupby('device_id').describe()
    device_stats = device_stats.reset_index()
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
    zone_stats = (
        df.groupby('zone')['moisture_level'].mean()
        .reset_index(name="avg_moisture")
    )
    min_risk_percent = 30
    zone_stats['high_risk'] = zone_stats['avg_moisture'] < min_risk_percent
    risky_zone_ids = zone_stats['zone'].unique()
    return zone_stats, risky_zone_ids


device_stats = per_device_stats(df)
device_stats.to_json("data/device_stats.json", indent=4, orient="records")
