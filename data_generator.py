import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_data(num_rows=100):
    np.random.seed(42)

    lead_ids = np.arange(1000, 1000 + num_rows)
    deal_stages = ['Qualified', 'Proposal', 'Negotiation', 'Closed Won', 'Closed Lost']
    sources = ['Web', 'Email', 'Phone', 'Referral', 'Ad']

    data = {
        'lead_id': np.random.choice(lead_ids, size=num_rows),
        'lead_source': np.random.choice(sources, size=num_rows),
        'deal_stage': np.random.choice(deal_stages, size=num_rows),
        'deal_size': np.random.randint(500, 15000, size=num_rows),
        'created_date': [datetime.now() - timedelta(days=np.random.randint(1, 90)) for _ in range(num_rows)],
        'closed_date': [datetime.now() - timedelta(days=np.random.randint(1, 30)) for _ in range(num_rows)],
    }

    df = pd.DataFrame(data)

    # Randomly insert some nulls
    for col in ['lead_source', 'deal_stage']:
        df.loc[df.sample(frac=0.1).index, col] = np.nan

    return df