import pandas as pd

df = pd.read_csv('Clean/fact_attendance_monthly.csv')
print(df.columns.tolist())

# FIX: fakt number thev, shevatche 8 ank ghe (020250430 -> 20250430)
df['date_key'] = df['date_key'].astype(str).str.replace(r'\D', '', regex=True)
df['date_key'] = df['date_key'].str[-8:]

df['date_clean'] = pd.to_datetime(df['date_key'], format='%Y%m%d')
df['year_month'] = df['date_clean'].dt.strftime('%Y-%m')
df['month_num'] = df['date_clean'].dt.month

df.to_csv('Clean/fact_attendance_monthly_CLEAN.csv', index=False)
print("Clean file saved! Rows:", len(df))
print(df.head())