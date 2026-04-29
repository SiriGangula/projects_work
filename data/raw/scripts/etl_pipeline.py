import pandas as pd
from datetime import datetime
from pathlib import Path


RAW_FILE_PATH = Path("data/raw/sales_data.csv")
CURATED_FILE_PATH = Path("output/curated_sales_data.csv")


def extract_data(file_path):
    """Extract raw sales data from CSV."""
    try:
        df = pd.read_csv(file_path)
        print(f"Extracted {len(df)} records from {file_path}")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file not found: {file_path}")


def transform_data(df):
    """Clean, validate, and transform raw sales data."""

    # Remove duplicate transactions
    df = df.drop_duplicates(subset=["transaction_id"])

    # Drop rows with missing critical values
    required_columns = [
        "transaction_id",
        "customer_id",
        "product_category",
        "quantity",
        "unit_price",
        "transaction_date",
        "region"
    ]
    df = df.dropna(subset=required_columns)

    # Convert date column
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])

    # Calculate total sales amount
    df["total_amount"] = df["quantity"] * df["unit_price"]

    # Add year, month, and day fields for analytics
    df["transaction_year"] = df["transaction_date"].dt.year
    df["transaction_month"] = df["transaction_date"].dt.month
    df["transaction_day"] = df["transaction_date"].dt.day

    # Add audit column
    df["etl_processed_timestamp"] = datetime.now()

    # Reorder columns
    final_columns = [
        "transaction_id",
        "customer_id",
        "product_category",
        "product_name",
        "quantity",
        "unit_price",
        "total_amount",
        "transaction_date",
        "transaction_year",
        "transaction_month",
        "transaction_day",
        "region",
        "payment_method",
        "etl_processed_timestamp"
    ]

    df = df[final_columns]

    print(f"Transformed data. Final record count: {len(df)}")
    return df


def load_data(df, output_path):
    """Load curated data to output folder."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Curated data written to {output_path}")


def run_etl_pipeline():
    """Run end-to-end ETL pipeline."""
    raw_df = extract_data(RAW_FILE_PATH)
    curated_df = transform_data(raw_df)
    load_data(curated_df, CURATED_FILE_PATH)


if __name__ == "__main__":
    run_etl_pipeline()
