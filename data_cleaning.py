# File: data_cleaning.py
# Cleans and standardizes data

def clean_data(df):
    df = df.dropna(subset=['Lead ID'])
    df = df.drop_duplicates()
    df['Create Date'] = pd.to_datetime(df['Create Date'], errors='coerce')
    df['Deal Amount'] = df['Deal Amount'].fillna(0)
    df['Lead Source'] = df['Lead Source'].fillna('Unknown')
    return df
