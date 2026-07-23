# Project DE ETL

Project ini adalah contoh ETL sederhana menggunakan Python, Airflow, dan PostgreSQL.

## Fitur
- Mengambil data dari Open Library API
- Membersihkan dan memformat data buku
- Menyimpan data ke PostgreSQL melalui Airflow DAG

## Struktur Project
- `extract_and_cleaning_data.py` : script ekstraksi dan pembersihan data standalone
- `airflow/dags/dags_etl.py` : DAG Airflow untuk menjalankan ETL
- `airflow/dags/files/create_table.sql` : query pembuatan tabel PostgreSQL
- `compose.yml` : konfigurasi Docker Compose untuk menjalankan Airflow dan PostgreSQL

## Cara Menjalankan

### 1. Buat environment virtual
```bash
python -m venv myvenv
source myvenv/bin/activate
```

### 2. Install dependency
```bash
pip install -r requirements.txt
```

### 3. Jalankan dengan Docker Compose
```bash
docker compose up -d
```

### 4. Akses Airflow
Buka browser ke:
```text
http://localhost:8080
```

## Catatan
Pastikan file `.env` dibuat berdasarkan `.env.example` sebelum menjalankan aplikasi.
