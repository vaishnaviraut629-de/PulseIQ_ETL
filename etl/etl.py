import os
import pandas as pd
from sqlalchemy import create_engine
import glob

DB_USER = os.getenv("POSTGRES_USER", "pulsiq")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "pulsiq123")
DB_NAME = os.getenv("POSTGRES_DB", "warehouse")
DB_HOST = os.getenv("DB_HOST", "db")

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}")

excel_file = "03_PulseIQ_Analytics_Star_Schema_Dataset.xlsx"
print(f"Reading {excel_file}...")
xls = pd.ExcelFile(excel_file)
for sheet in xls.sheet_names:
    print(f"Loading sheet: {sheet}")
    df = pd.read_excel(excel_file, sheet_name=sheet)
    table_name = sheet.lower().replace(" ", "_").replace("-", "_")
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f" -> Inserted {len(df)} rows into {table_name}")

print("ETL Completed Successfully!")