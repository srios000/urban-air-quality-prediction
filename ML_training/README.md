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
/src/data_processing    # script untuk data processing
/src/models             # model definitions dan training scripts
/tests              # script untuk inference tests
```

## Setup

1. Clone repository ini

```bash

git clone https://github.com/srios000/urban-air-quality-prediction.git
cd urban-air-quality-prediction
```

2. Buat virtual environment

```bash
conda create -n main python=3.12
```

3. Install dependencies

```bash
pip install -r ML_training/requirements.txt
```

4. Jalankan script main untuk memulai training model

```bash
python ML_training/main.py
```
