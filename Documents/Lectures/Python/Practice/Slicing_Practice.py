# import csv
# import json
# import numpy as np
# from datetime import datetime, timedelta
# import os
#
# # --- DEFINE YOUR STRUCTURED ARRAY DATA TYPES ---
# # HINT: dtype=[('field_name', type), ...]. Use 'U20' for <=20 char strings, 'f8' for float64, 'i4' for int32
# # You'll need one for input reading, one for the final anomaly array (same fields)
# INPUT_DTYPE = np.dtype([
#     ('timestamp', 'U25'),
#     ('sensor_id', 'U10'),
#     ('moisture_level', 'f8'),
#     ('temperature', 'f8')
# ])
# ANOMALY_DTYPE = INPUT_DTYPE # Same structure
#
# def load_sensor_data(filename):
#     # 1. READ CSV USING csv module -> List of Dicts
#     # 2. CLEAN DATA (missing, ranges, types) -> Remove invalid rows (except missing moisture, which fails!)
#     # 3. Convert cleaned list of dicts to NumPy structured array using INPUT_DTYPE
#     # 4. Return numpy array or raise error if no valid data
#     raw_data_list =
#     valid_data =
#     print(f"Loading data from {filename}...")
#     try:
#         with open(filename, 'r', newline='') as f:
#             reader = csv.DictReader(f)
#             for i, row in enumerate(reader):
#                 raw_data_list.append(row)
#     except FileNotFoundError:
#         print(f"Error: Data file {filename} not found.")
#         return np.array(, dtype=INPUT_DTYPE) # Return empty on failure
#     except Exception as e:
#         print(f"Error reading CSV file {filename}: {e}")
#         return np.array(, dtype=INPUT_DTYPE)
#
#     # Now process the raw_data_list for cleaning...<FILL IN>
#     # Validation: Check for missing moisture_level -> CRITICAL
#     # Validation: moisture_level 0-100, temperature -20 to 60, timestamp non-empty
#     # If invalid (except missing hydro) remove and warn: print(f"INFO: Row {i+2} skipped due to invalid/missing data: {row}")
#     # If moisture_level is missing/invalid, STOP processing (cannot analyze)
#
#     if not valid_data:
#         print("WARNING: No valid data after cleaning. Returning empty array.")
#         return np.array(, dtype=INPUT_DTYPE)
#     # Convert valid_data (list of dicts) to numpy structured array
#     # HINT: np.array([tuple(d.values()) for d in valid_data], dtype=INPUT_DTYPE)
#     return np.array(, dtype=INPUT_DTYPE) # Placeholder return
#
# def calculate_stats(data_array):
#     # 1. Group data_array by sensor_id (use np.where + loop, or manual grouping)
#     # 2. For each group, extract moisture_levels -> 1D array
#     # 3. Use np.mean(), np.std()
#     # 4. Return dict {sensor_id: {"mean": x, "std": y, "count": N}}
#     stats = {}
#     if data_array.size == 0:
#         return stats
#     # Extract unique sensor IDs
#     sensor_ids = np.unique(data_array['sensor_id'])
#     for sensor_id in sensor_ids:
#         # Create a boolean mask for this sensor
#         mask = data_array['sensor_id'] == sensor_id
#         sensor_data = data_array[mask]['moisture_level']
#         mean_val = np.mean(sensor_data)
#         std_val = np.std(sensor_data)
#         count = sensor_data.size
#         stats[sensor_id] = {"mean": float(mean_val), "std": float(std_val), "count": int(count)}
#     return stats
#
# def detect_anomalies(data_array, stats_dict, threshold=2.0):
#     # 1. Use vectorized operations to calculate z-score for each moisture_level
#     #    z = (reading - sensor_mean) / sensor_std -> Use stats_dict[sensor_id]['mean/std']
#     #    Handle std=0! If std is 0, set z=0 (no variation, so no anomaly), or flag?
#     # 2. Use boolean condition (abs(z) > threshold) to filter
#     # 3. Return new NumPy array of only the anomaly records (same dtype ANOMALY_DTYPE)
#     if data_array.size == 0:
#         return np.array(, dtype=ANOMALY_DTYPE)
#
#     # Prepare arrays for vectorized calculation
#     readings = data_array['moisture_level']
#     sensor_ids = data_array['sensor_id']
#     z_scores = np.zeros(readings.shape) # Initialize
#
#     # Loop through unique sensors to get their stats (cannot broadcast stats_dict directly)
#     for sensor_id in np.unique(sensor_ids):
#         sensor_stat = stats_dict.get(sensor_id)
#         if sensor_stat is None or sensor_stat["count"] < 2: # Need stats AND multiple readings to calculate std
#              sensor_mask_for_stats = (sensor_ids == sensor_id)
#              z_scores[sensor_mask_for_stats] = 0.0 # Not enough data for reliable z-score
#              continue
#         sensor_mean = sensor_stat["mean"]
#         sensor_std = sensor_stat["std"]
#         sensor_mask = (sensor_ids == sensor_id)
#
#         if sensor_std == 0:
#             z_scores[sensor_mask] = 0.0 # No std, no anomaly defined
#         else:
#             sensor_readings = readings[sensor_mask]
#             z = (sensor_readings - sensor_mean) / sensor_std
#             z_scores[sensor_mask] = z
#
#     # Detect anomalies: absolute z-score > threshold
#     anomaly_mask = np.abs(z_scores) > threshold
#
#     # Extract anomalies
#     anomalies = data_array[anomaly_mask] # This works for structured arrays!
#
#     return np.array(anomalies, dtype=ANOMALY_DTYPE) # Ensure correct dtype
#
# def generate_report(anomalies_array, stats_dict):
#     # 1. Calculate total readings (from main script, ideally passed in or recalculated from stats?)
#     #    Simpler: get from main script logic (basic count of original)
#     #    Or: sum(stats_dict[device]['count'] for device in stats_dict) -> Total readings
#     total_readings = sum(v['count'] for v in stats_dict.values())
#     total_anomalies = anomalies_array.size
#     anomalous_moisture = anomalies_array['moisture_level'] if total_anomalies > 0 else np.array()
#     anomalous_z_scores =  # How to get? Need to recalculate from main logic? HARD LINK.
#     # *** IMPORTANT: To get max/min z-score, you need to calculate the z-scores for the ANOMALOUS readings ***
#     # Do it here simplistically: loop through anomalies and apply z=(x-mean)/std from stats_dict
#     if total_anomalies > 0:
#         anomalous_z_calculated =
#         for i in range(anomalies_array.size):
#             rec = anomalies_array[i]
#             sid = rec['sensor_id']
#             reading = rec['moisture_level']
#             smean = stats_dict[sid]['mean']
#             sstd = stats_dict[sid]['std']
#             if sstd > 0:
#                 z = (reading - smean) / sstd
#                 anomalous_z_calculated.append(z)
#         anomalous_z_array = np.array(anomalous_z_calculated)
#         max_z = float(np.max(np.abs(anomalous_z_array))) if anomalous_z_array.size > 0 else 0.0
#         mean_anomalous_moisture = float(np.mean(anomalous_moisture)) if anomalous_moisture.size > 0 else 0.0
#     else:
#         max_z = 0.0
#         mean_anomalous_moisture = 0.0
#
#     anomalies_per_sensor = {}
#     if total_anomalies > 0:
#         unique_sensors, counts = np.unique(anomalies_array['sensor_id'], return_counts=True)
#         anomalies_per_sensor = dict(zip(unique_sensors, counts))
#
#     # 2. PRINT Summary to Console
#     print("
