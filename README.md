# Sistem Prediksi Kualitas Udara Perkotaan

## Deskripsi
Proyek ini mengembangkan sistem prediksi kualitas udara berbasis machine learning yang dapat memprediksi indeks kualitas udara (Air Quality Index/AQI) secara harian berdasarkan data historis polutan.

## Anggota Tim
- A002YBF021 – Agung Kurniawan – Institut Teknologi Bandung
- A135YAM326 – Muhammad Husain – Politeknik Negeri Ujung Pandang
- A009YBF463 – Sintario Satya – Universitas Gunadarma
- A135XAF486 – Tsamarah Muthi'ah Abdullah – Politeknik Negeri Ujung Pandang

## Struktur Proyek
```
/data               # untuk raw data dan processed data 
/notebooks          # untuk eksplorasi data dan prototyping
/src                # source code utama
/data_processing    # script untuk data processing
/models             # model definitions dan training scripts
/api                # kode untuk API
/visualization      # kode untuk visualisasi
/tests              # unit tests
/docs               # dokumentasi
/config             # file konfigurasi
```

## Setup
1. Clone repository ini
```bash

git clone https://github.com/srios000/urban-air-quality-prediction.git
cd urban-air-quality-prediction
```

2. Buat virtual environment
```bash
python -m venv env
source env/bin/activate  # Untuk Linux/Mac
env\Scripts\activate     # Untuk Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Copy file .env.example menjadi .env dan sesuaikan konfigurasi
```bash
cp .env.example .env
# Edit file .env dengan konfigurasi lokal masing - masing
```
