# File: data_generator.py
# Simulates raw sales/CRM data input
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_data():
    np.random.seed(42)
    num_records = 100
    dates = [datetime.now() - timedelta(days=np.random.randint(0, 60)) for _ in range(num_records)]
    stages = ['Prospect', 'Qualified', 'Proposal', 'Closed Won', 'Closed Lost']

    data = {
        'Lead ID': [f'L{1000 + i}' for i in range(num_records)],
        'Lead Source': np.random.choice(['Web', 'Email', 'Referral', 'Event', None], num_records),
        'Create Date': [d.strftime('%m/%d/%Y') for d in dates],
        'Deal Stage': np.random.choice(stages, num_records),
        'Deal Amount': np.random.choice([5000, 10000, 20000, None], num_records),
    }

    df = pd.DataFrame(data)
    df.loc[df.sample(frac=0.1).index, 'Lead ID'] = None  # Introduce some nulls
    df = pd.concat([df, df.sample(10)])  # Add duplicates
    return df
