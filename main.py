import pandas as pd

df = pd.read_csv('World-happiness-report-2024 (1).csv')
print(df.describe())
print(df.info())

