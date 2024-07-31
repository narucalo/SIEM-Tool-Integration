# SIEM Tool Integration Project Documentation

## Overview
This project integrates with Splunk to collect, analyze, and visualize security event data. It includes scripts for data ingestion, analysis, and visualization, along with configuration files and tests.

## Project Structure
- `config/`: Configuration files.
- `data/`: Sample and processed data.
- `scripts/`: Python scripts for data operations.
- `tests/`: Unit tests for the scripts.
- `dashboards/`: Custom Splunk dashboards.
- `docs/`: Documentation and user guides.
- `logs/`: Log files.

## Setup
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies using `pip install -r requirements.txt`.
4. Configure Splunk connection details in `config/config.ini`.

## Usage
1. Run the data ingestion script to send sample data to Splunk.
   ```sh
   python scripts/ingest_data.py
