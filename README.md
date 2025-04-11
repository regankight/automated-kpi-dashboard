# Automated KPI Report Pipeline – Simulated Sales Dashboard Refresh

## Overview

This project simulates an automated KPI reporting pipeline using Python, demonstrating key skills in data automation, data cleaning, KPI calculation, and reporting workflows. It reflects the kind of real-world automation I developed at Smarsh, GoRefime, and during freelance projects.

## Use Case

The project showcases how to build a lightweight automated reporting solution without needing heavy backend infrastructure. It combines data cleaning, KPI calculation, and a simulated refresh process, similar to how BI and RevOps teams streamline reporting workflows.

## Key Features

- **Data Generation:** Simulates messy, real-world CRM data (incomplete, duplicated, and inconsistent).
- **Data Cleaning:** Standardizes data, handles nulls, and removes duplicates.
- **KPI Calculation:** Computes conversion rates, average deal size, and average deal velocity.
- **Automated Refresh Simulation:** Uses a simple schedule to mimic a weekly update.
- **Failure Alert Simulation:** Provides basic error handling through simulated alerts.

## Technologies Used

- **Python:** Core logic and automation simulation.
- **Pandas:** Data manipulation and cleaning.
- **NumPy:** Data generation and randomization.
- **Time:** Simulated scheduling.

## Project Structure

```
automated-kpi-dashboard/
├── data_generator.py       # Simulates messy CRM data
├── data_cleaning.py        # Cleans and standardizes data
├── kpi_calculator.py       # Calculates key sales metrics
├── report_refresher.py     # Legacy runner (replaced by main.py)
├── notification_sim.py     # Simulates failure notifications
├── output/                 # Folder for saved .csv report
├── main.py                 # Runs the full pipeline
└── README.md               # Project documentation
```

## Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/regankight/automated-kpi-dashboard.git
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

3. View the KPI report in your terminal and as a CSV in the `output/` folder.

## Why This Matters

This project demonstrates my ability to combine BI logic and process automation to produce repeatable, reliable insights. These are skills I developed at Smarsh, GoRefime, and through freelance work. By simulating real-world data challenges, it highlights how to maintain data quality while automating reporting.

## Connect with Me

Check out more of my work on GitHub or [LinkedIn](https://www.linkedin.com/in/regankight).
