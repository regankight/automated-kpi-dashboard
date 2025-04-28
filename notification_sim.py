"""Simulates sending alerts if pipeline errors occur."""
def notify_failure(error_message):
    print("\n❌ Pipeline failed.")
    print(f"Error: {error_message}")
