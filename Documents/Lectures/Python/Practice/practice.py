import pandas as pd
import os

print("Files in data/ :", os.listdir("data/"))

df_a = pd.read_csv("data/site_a_readings.csv")