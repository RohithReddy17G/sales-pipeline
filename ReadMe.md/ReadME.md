# Automated Sales ETL Pipeline

An end-to-end Python and SQL data engineering pipeline that ingests raw sales transaction records, cleans missing and inconsistent fields, loads the data into a SQLite database, and executes analytical SQL queries to calculate business metrics.

## Features
- **Extraction:** Reads raw transaction records from CSV files using `pandas`.
- **Transformation:** Handles missing customer names, trims whitespace from order statuses, and calculates total sales amounts dynamically.
- **Loading:** Creates and writes structured tables to a local `SQLite` database.
- **Analytics:** Runs aggregate SQL queries (`GROUP BY`, `SUM`, `COUNT`) to produce summary reports.

## Project Structure
- `pipeline.py`: Main Python script containing extraction, transformation, and database loading logic.
- `raw_sales.csv`: Raw sample dataset containing e-commerce transaction logs.
- `README.md`: Project documentation and setup guide.

## How to Run
1. Run the ETL pipeline script:
   ```bash
   python pipeline.py