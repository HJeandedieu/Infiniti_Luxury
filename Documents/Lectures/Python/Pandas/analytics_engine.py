import pandas as pd
import numpy as np
import json

#Load data
df = pd.read_csv("data/sensor_logs_zone.csv", parse_dates=['timestamp'], index_col=['timestamp'])
print(f"Loaded {len(df)} sensor logs with {df['device_id'].nunique()} devices.")

# Sample working functions

def compute_device_stats(df, device_id):
    # Return dict of stats for a single device\
    pass

def get_anomalous_readings(device_series, threshold = 2):
    # Use z-score to identify outliers
    pass

def analyze_by_zone(df, min_risk_percent = 30):
    # Use boolean indexing to find high-risk zones
    pass

