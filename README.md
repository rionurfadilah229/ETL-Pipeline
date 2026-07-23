# ETL Pipeline Project

Project ini adalah contoh implementasi ETL sederhana menggunakan Python, Apache Airflow, dan PostgreSQL untuk mengambil, membersihkan, dan menyimpan data buku dari Open Library API.

## Overview
Proyek ini menunjukkan alur kerja data engineering dasar yang mencakup:
- ekstraksi data dari sumber eksternal
- transformasi dan pembersihan data
- loading data ke database relasional
- orkestrasi proses menggunakan Airflow

## Output ETL dalam Konteks Kerjaan
Hasil dari pipeline ini adalah data buku yang telah diproses dan siap digunakan untuk kebutuhan bisnis maupun analitik, seperti:
- data terstruktur untuk laporan dan dashboard
- data yang tersimpan di PostgreSQL untuk kebutuhan query dan analisis
- pipeline otomatis yang memudahkan proses pengolahan data secara berulang

Dengan demikian, project ini merepresentasikan alur ETL yang berguna untuk mendukung pengambilan keputusan, analisis data, dan otomasi proses data.

## Project Structure
- [extract_and_cleaning_data.py](extract_and_cleaning_data.py) — script standalone untuk ekstraksi dan pembersihan data
- [airflow/dags/dags_etl.py](airflow/dags/dags_etl.py) — DAG Airflow untuk menjalankan pipeline ETL
- [airflow/dags/files/create_table.sql](airflow/dags/files/create_table.sql) — SQL untuk membuat tabel di PostgreSQL
- [compose.yml](compose.yml) — konfigurasi Docker Compose untuk menjalankan Airflow dan PostgreSQL

## Tech Stack
- Python
- Apache Airflow
- PostgreSQL
- Docker Compose
- Requests

## Getting Started

### 1. Create virtual environment
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

### 4. Access Airflow UI
Open your browser and go to:
```text
http://localhost:8080
```

## Notes
Make sure to create a `.env` file based on [.env.example](.env.example) before running the application.
