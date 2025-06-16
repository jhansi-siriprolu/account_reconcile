import pandas as pd

def preprocess_data(df, source='bank'):
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df['description'] = df['description'].fillna("").str.lower().str.replace(r'[^a-z0-9 ]', '', regex=True)
    df['clean_desc'] = df['description'].str.extract(r'(counter \d+)', expand=False).fillna("unknown")
    if source == 'bank':
        df.set_index('bank_id', inplace=True)
    else:
        df.set_index('ledger_id', inplace=True)
    return df