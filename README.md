# SIEM Tool Integration Project

## Project Setup
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies using `pip install -r requirements.txt`.
4. Configure Splunk connection details in `config/splunk_config.py`.

## Scripts
- `data_ingestion.py`: Script to ingest data into Splunk.
- `data_analysis.py`: Script to analyze data using Splunk queries.
- `custom_visualization.py`: Script to create custom visualizations.

## Usage
1. Run the data ingestion script to send sample data to Splunk.
   ```sh
   python scripts/data_ingestion.py

