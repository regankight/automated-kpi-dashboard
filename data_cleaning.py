"""Cleans and standardizes CRM data for KPI calculation."""
import pandas as pd

def clean_data(df):
    # Drop rows with missing critical fields
    df = df.dropna(subset=['lead_id', 'lead_source', 'deal_stage'])

    # Remove duplicates
    df = df.drop_duplicates(subset=['lead_id'])

    # Format dates
    df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
    df['closed_date'] = pd.to_datetime(df['closed_date'], errors='coerce')

    # Filter out rows with invalid or missing dates
    df = df.dropna(subset=['created_date', 'closed_date'])

    # Make sure deal_size is numeric
    df['deal_size'] = pd.to_numeric(df['deal_size'], errors='coerce')
    df = df.dropna(subset=['deal_size'])

    return df
