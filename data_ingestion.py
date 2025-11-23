import pandas as pd
import os

df = pd.read_csv("tourism_project/data/tourism.csv")
df.to_csv("tourism_project/data/raw_data.csv", index=False)

print("Data ingestion completed.")
