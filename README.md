# Serverless Sales ETL Pipeline using Python and AWS

## Project Overview

This project demonstrates a data engineering ETL pipeline built using Python and AWS-aligned architecture. The pipeline extracts raw sales transaction data, performs data cleaning and transformation, validates records, and generates analytics-ready curated output.

The project is designed to simulate a real-world cloud data pipeline where raw files are stored in Amazon S3, processed using Python or AWS Glue, and prepared for loading into Amazon Redshift or another analytics warehouse.

## Tech Stack

- Python
- Pandas
- AWS S3
- AWS Glue
- AWS Lambda
- Amazon Redshift
- GitHub
- ETL / Data Pipeline Design

## Architecture

1. Raw sales data lands in the raw data layer.
2. Python ETL script reads the raw CSV file.
3. Data is cleaned, validated, and transformed.
4. Business metrics are calculated.
5. Curated output is written for analytics and reporting.

## Pipeline Layers

- Raw Layer: Original source files
- Processed Layer: Cleaned and validated records
- Curated Layer: Business-ready dataset for analytics

## Features

- Reads raw CSV sales transaction data
- Handles missing values
- Removes duplicate transactions
- Standardizes date fields
- Calculates revenue metrics
- Adds audit columns
- Writes curated output as CSV
- Designed to be extended with AWS S3, Glue, Lambda, and Redshift

## Sample Use Case

This pipeline can be used by a retail or e-commerce company to process daily sales transactions and prepare clean datasets for dashboards, reporting, and business analysis.

## Future Enhancements

- Store raw and curated files in Amazon S3
- Convert CSV output to Parquet
- Use AWS Glue for large-scale transformation
- Trigger pipeline using AWS Lambda
- Load curated data into Amazon Redshift
- Add Airflow orchestration
