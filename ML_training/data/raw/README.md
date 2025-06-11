# Dataset Kualitas Udara
## Gambaran Umum
Dataset ini berisi data kualitas udara yang telah diproses, yang awalnya diperoleh dari [AQICN.org](https://aqicn.org/historical/). Data mentah dari aqicn telah melalui proses engineering untuk menghitung nilai EPA AQI (Air Quality Index) yang terstandarisasi untuk analisis dan perbandingan yang lebih baik.

## Sumber Data
- **Sumber Asli**: [AQICN Historical Data](https://aqicn.org/historical/)
- **Format Data**: File CSV
- **Cakupan**: Beberapa lokasi dengan pengukuran kualitas udara historis

## Proses Data Engineering
### Langkah-langkah Pemrosesan Utama
1. **Standardisasi Data**: Nama kolom dinormalisasi untuk konsistensi
2. **Konversi Unit**: Data AQICN (μg/m³) dikonversi ke unit standar EPA bila diperlukan
3. **Perhitungan AQI**: Nilai EPA AQI dihitung menggunakan breakpoint resmi
4. **Validasi Data**: Pengecekan batas nilai yang masuk akal dan penanganan outlier
5. **Penggabungan Data**: Semua file lokasi digabungkan menjadi satu dataset

### Polutan yang Diproses
- **PM2.5** (Particulate Matter ≤ 2.5μm) - μg/m³
- **PM10** (Particulate Matter ≤ 10μm) - μg/m³  
- **O3** (Ozone) - dikonversi dari μg/m³ ke ppm
- **NO2** (Nitrogen Dioxide) - dikonversi dari μg/m³ ke ppm
- **SO2** (Sulfur Dioxide) - dikonversi dari μg/m³ ke ppm
- **CO** (Carbon Monoxide) - dikonversi dari μg/m³ ke ppm

### Konversi Unit yang Diterapkan
Faktor konversi berikut digunakan untuk mengkonversi nilai AQICN μg/m³ ke unit ppm standar EPA (pada 25°C, 1 atm):
- **O3**: 1/1962 (μg/m³ ke ppm)
- **NO2**: 1/1882 (μg/m³ ke ppm)
- **SO2**: 1/2619 (μg/m³ ke ppm)
- **CO**: 1/1145 (μg/m³ ke ppm)

### Perhitungan EPA AQI
Nilai AQI dihitung menggunakan breakpoint resmi EPA untuk setiap polutan:
- **Good**: 0-50
- **Moderate**: 51-100
- **Unhealthy for Sensitive Groups**: 101-150
- **Unhealthy**: 151-200
- **Very Unhealthy**: 201-300
- **Hazardous**: 301-500

AQI keseluruhan ditentukan oleh nilai AQI polutan individu yang tertinggi.

## Struktur Dataset
### Kolom Utama
- `date` - Tanggal pengukuran (datetime)
- `loc` - Identifier lokasi
- `pm25` - Konsentrasi PM2.5 (μg/m³)
- `pm10` - Konsentrasi PM10 (μg/m³)
- `o3` - Konsentrasi Ozone (μg/m³ asli)
- `no2` - Konsentrasi NO2 (μg/m³ asli)
- `so2` - Konsentrasi SO2 (μg/m³ asli)
- `co` - Konsentrasi CO (μg/m³ asli)
- `aqi` - Nilai EPA AQI yang dihitung

## Fitur Kualitas Data
### Langkah-langkah Validasi
- **Parsing Numerik**: Penanganan untuk konversi string/numerik
- **Pengecekan Range**: Nilai divalidasi terhadap rentang konsentrasi polutan yang masuk akal
- **Data Hilang**: Penanganan proper untuk nilai null/kosong
- **Deteksi Outlier**: Nilai AQI tinggi (≥200) ditandai untuk review

## Catatan
### Keandalan Data
- Perhitungan AQI mengikuti metodologi resmi EPA
- Konversi unit memastikan konsistensi dengan standar EPA  
- Nilai AQICN asli tetap dipertahankan bersama dengan AQI yang dihitung

---
*Dataset ini telah diproses untuk menyediakan nilai AQI yang terstandarisasi dan sesuai dengan EPA untuk tujuan analisis dan penelitian kualitas udara.*