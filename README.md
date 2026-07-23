# ETL Pipeline Project

This project is a simple ETL implementation using Python, Apache Airflow, and PostgreSQL to extract, clean, and store book data from the Open Library API.

## Overview
This project demonstrates a basic data engineering workflow that includes:
- extracting data from an external source
- transforming and cleaning the data
- loading the data into a relational database
- orchestrating the process using Airflow

## ETL Output 
The output of this pipeline is processed book data that is ready to be used for business and analytical purposes, such as:
- structured data for reporting and dashboards
- data stored in PostgreSQL for querying and analysis
- an automated pipeline that simplifies repeated data processing tasks

In this way, the project represents an ETL workflow that supports decision-making, data analysis, and data automation.

## Project Structure
- [extract_and_cleaning_data.py](extract_and_cleaning_data.py) — standalone script for extracting and cleaning data
- [airflow/dags/dags_etl.py](airflow/dags/dags_etl.py) — Airflow DAG for running the ETL pipeline
- [airflow/dags/files/create_table.sql](airflow/dags/files/create_table.sql) — SQL script to create tables in PostgreSQL
- [compose.yml](compose.yml) — Docker Compose configuration for running Airflow and PostgreSQL

## Tech Stack
- Python
- Apache Airflow
- PostgreSQL
- Docker Compose
- Requests

## Getting Started

### 1. Create a virtual environment
```bash
python -m venv myvenv
source myvenv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run with Docker Compose
```bash
docker compose up -d
```

### 4. Access the Airflow UI
Open your browser and go to:
```text
http://localhost:8080
```

## Notes
Make sure to create a `.env` file based on [.env.example](.env.example) before running the application.
