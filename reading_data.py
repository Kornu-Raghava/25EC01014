import pandas as pd

file_path = r"C:\Users\Satya\Desktop\LABS\EDA TASKS\Electrical Data\MOSFET_ID_VDS.csv"

df = pd.read_csv(file_path)

print("Columns:")
print(df.columns)

print("\nShape (rows, columns):")
print(df.shape)

print("\nSummary statistics:")
print(df.describe())
