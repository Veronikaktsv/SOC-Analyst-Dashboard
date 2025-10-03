look # SOC Analyst Dashboard

This project provides an interactive dashboard for SOC Analysts to monitor key security operation center (SOC) metrics such as Mean Time to Detect (MTTD), Mean Time to Respond (MTTR), and incident counts by type and severity.

## Features

- Calculates and displays MTTD and MTTR from incident timestamps.
- Visualizes incident counts by type using bar charts.
- Visualizes incident counts by severity using pie charts.
- Interactive dashboard built with Plotly Dash.

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/SOC-Analyst-Dashboard.git
    cd SOC-Analyst-Dashboard
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
3. Run the dashboard:

   ```bashe
   python app.py
4. Open your browser and navigate to:

   ```bash
   http://127.0.0.1:8050
## Data Format
The dashboard expects incident data in incidents.csv with the following columns:

- `incident_id`: Unique incident identifier
- `start_time`: Incident start time (YYYY-MM-DD HH:MM)
- `detect_time`: Time the incident was detected
- `resolve_time`: Time the incident was resolved
- `type`: Incident type (e.g., Phishing, Malware, Brute Force)
- `severity`: Severity level (Low, Medium, High)

## Example Data

   ```bash
    incident_id,start_time,detect_time,resolve_time,type,severity
    INC001,2025-08-01 09:00,2025-08-01 09:45,2025-08-01 10:30,Phishing,High
    INC002,2025-08-01 10:15,2025-08-01 11:00,2025-08-01 12:00,Malware,Medium
   ```

License
This project is licensed under the [MIT License](LICENSE).
