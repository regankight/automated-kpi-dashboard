# File: notification_sim.py
# Fake email alert on failure or outlier

def notify_failure(issue):
    print(f"[ALERT] Report refresh failed: {issue}")
