import sqlite3
import pandas as pd

# 1. Extract: Load raw CSV data
print("Extracting raw sales data...")
df = pd.read_csv("raw_sales.csv")

# 2. Transform: Clean missing values and format fields
print("Transforming data...")
df["Customer_Name"] = df["Customer_Name"].fillna("Unknown")
df["Status"] = df["Status"].str.strip().str.capitalize()
df["Total_Amount"] = df["Quantity"] * df["Price_Per_Unit"]

# 3. Load: Save cleaned data into SQLite database
print("Loading data into SQLite database...")
conn = sqlite3.connect("sales_data.db")
df.to_sql("cleaned_sales", conn, if_exists="replace", index=False)

# 4. Analyze: Run SQL aggregation query
query = """
SELECT 
    Status, 
    COUNT(Order_ID) AS Total_Orders, 
    SUM(Total_Amount) AS Revenue 
FROM cleaned_sales 
GROUP BY Status;
"""
summary_df = pd.read_sql_query(query, conn)
print("\n--- Sales Summary by Status ---")
print(summary_df)

conn.close()
print("\nETL Pipeline Execution Complete!")