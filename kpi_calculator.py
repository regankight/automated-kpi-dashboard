# File: kpi_calculator.py
# Calculate sales KPIs

def calculate_kpis(df):
    total_leads = len(df)
    closed_won = df[df['Deal Stage'] == 'Closed Won']
    closed_lost = df[df['Deal Stage'] == 'Closed Lost']

    conversion_rate = len(closed_won) / total_leads if total_leads else 0
    avg_deal_size = closed_won['Deal Amount'].mean() if not closed_won.empty else 0

    if not df.empty:
        df['Days to Close'] = (pd.Timestamp.now() - df['Create Date']).dt.days
        avg_velocity = df[df['Deal Stage'] == 'Closed Won']['Days to Close'].mean()
    else:
        avg_velocity = 0

    return {
        'Total Leads': total_leads,
        'Conversion Rate': round(conversion_rate, 2),
        'Average Deal Size': round(avg_deal_size, 2),
        'Average Deal Velocity (days)': round(avg_velocity, 2) if avg_velocity else 0
    }
