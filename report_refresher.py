# File: report_refresher.py
# Simulates a scheduled weekly refresh
import time
from data_generator import generate_mock_data
from data_cleaning import clean_data
from kpi_calculator import calculate_kpis
from notification_sim import notify_failure

def refresh_report():
    print("Running report refresh...")
    try:
        raw = generate_mock_data()
        cleaned = clean_data(raw)
        kpis = calculate_kpis(cleaned)

        print("\nKPI Report:")
        for k, v in kpis.items():
            print(f"{k}: {v}")

        print("\nReport refreshed successfully at:", time.ctime())
    except Exception as e:
        notify_failure(str(e))
