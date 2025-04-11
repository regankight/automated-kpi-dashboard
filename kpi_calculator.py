def calculate_kpis(df):
    total_leads = len(df)
    closed_won = df[df['deal_stage'] == 'Closed Won']
    conversion_rate = len(closed_won) / total_leads if total_leads else 0

    avg_deal_size = closed_won['deal_size'].mean() if not closed_won.empty else 0

    # Calculate velocity: days between created and closed
    df['velocity_days'] = (df['closed_date'] - df['created_date']).dt.days
    avg_velocity = df['velocity_days'].mean() if not df.empty else 0

    return {
        'Total Leads': total_leads,
        'Conversion Rate': round(conversion_rate, 2),
        'Average Deal Size': round(avg_deal_size, 2),
        'Average Deal Velocity (days)': int(avg_velocity)
    }