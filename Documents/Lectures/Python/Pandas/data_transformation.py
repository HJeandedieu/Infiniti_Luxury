import pandas as pd

moisture_feed = pd.DataFrame({
    'zone_id': ['A1', 'A2', 'A3', 'A4'],
    'timestamp': pd.to_datetime(['2025-04-05 08:00', '2025-04-05 08:00','2025-04-05 08:00','2025-04-05 09:00']),
    'moisture_level': [0.65, 0.42,0.88, 0.58] # 0-1 scale: 0=very dry, 1=very wet
})

temp_feed = pd.DataFrame({
    'zone_id': ['A1', 'A2', 'A3', 'A1'],
    'timestamp': pd.to_datetime(['2025-04-05 08:00', '2025-04-05 08:00', '2025-04-05 08:00', '2025-04-05 09:00']),
    'temperature_c': [24.5, 26.1, 22.0, 27.3]  # degrees C
})

def merge_sensor_feeds(feed1, feed2, on_columns):
    # Merge two dataframes
    pass

result = merge_sensor_feeds(moisture_feed, temp_feed, on_columns=['zone_id', 'timestamp'])
print(result)

def pivot_feed_by_sensor(feed, index_col, columns_col, values_col):
    # Create pivot table
    pass

moisture_pivot = pivot_feed_by_sensor(
    moisture_feed,
    index_col = 'timestamp',
    columns_col = 'zone_id',
    values_col = 'moisture_level'
)
print(moisture_pivot)

def analyze_correlations(feed1, feed2, merge_keys, pivot_index, pivot_columns, values):
    # Chains the above to create a correlation-ready table
    pass

correlation_table = analyze_correlations(
    feed1=moisture_feed,
    feed2=temp_feed,
    merge_keys=['zone_id', 'timestamp'],
    pivot_index='timestamp',
    pivot_columns='zone_id',
    values=['moisture_level', 'temperature_c']
)
print(correlation_table)
# Min-max Normalization