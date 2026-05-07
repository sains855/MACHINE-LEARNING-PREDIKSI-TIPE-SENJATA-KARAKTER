# Dokumentasi Proyek: Genshin Impact Weapon Predictor

Dokumentasi ini memberikan panduan teknis mendalam mengenai struktur, pengembangan, dan penggunaan aplikasi prediksi senjata karakter Genshin Impact menggunakan Machine Learning.

---

## 1. Ikhtisar Proyek
Aplikasi ini dirancang untuk memprediksi jenis senjata yang paling sesuai bagi seorang karakter berdasarkan atribut statistik dasar. Proyek ini menggunakan algoritma klasifikasi yang dilatih pada dataset karakter Genshin Impact dan diimplementasikan melalui antarmuka web interaktif.

## 2. Struktur File Proyek
| Nama File | Deskripsi |
| :--- | :--- |
| `app.py` | Backend Flask yang menangani routing dan logika prediksi. |
| `PREDIKSI.ipynb` | Notebook Jupyter untuk Eksplorasi Data (EDA), preprocessing, dan pelatihan model. |
| `best_model.pkl` | Model Machine Learning (Decision Tree) yang telah dilatih. |
| `scaler.pkl` | Objek StandardScaler untuk normalisasi data fitur. |
| `label_encoder_weapon.pkl` | Encoder untuk mengubah target numerik kembali ke nama senjata asli. |
| `requirements.txt` | Daftar pustaka (library) Python yang diperlukan untuk menjalankan proyek. |
| `.gitignore` | Konfigurasi untuk mengecualikan file yang tidak perlu dari sistem kontrol versi. |

## 3. Alur Kerja Teknis

### A. Preprocessing & Eksplorasi (Notebook)
1.  **Analisis Fitur**: Mengidentifikasi fitur kunci seperti `Base HP`, `Base ATK`, `Base DEF`, `Element`, dan `Role`.
2.  **Encoding**: Menggunakan `LabelEncoder` untuk mengubah fitur kategorikal (teks) menjadi representasi numerik.
3.  **Penskalaan (Scaling)**: Menggunakan `StandardScaler` agar perbedaan rentang nilai antar statistik (misalnya HP ribuan vs ATK ratusan) tidak membingungkan model.
4.  **Pelatihan Model**: Berdasarkan pengujian, model terbaik dipilih dan diekspor menggunakan `joblib`.

### B. Implementasi Backend (`app.py`)
Aplikasi menggunakan Flask untuk menerima input dari form pengguna. Proses di balik layar meliputi:
1.  Menerima data statistik karakter.
2.  Mengubah data menjadi DataFrame pandas.
3.  Melakukan transformasi data menggunakan `scaler.pkl`.
4.  Melakukan prediksi menggunakan `best_model.pkl`.
5.  Mengembalikan hasil prediksi dalam bentuk nama senjata (misalnya: *Sword*, *Bow*).

## 4. Instalasi dan Penggunaan

### Prasyarat
- Python 3.8 atau lebih tinggi.
- Pip (Manajer paket Python).

### Langkah-langkah:
1.  **Instalasi Dependensi**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Menjalankan Aplikasi**:
    ```bash
    python app.py
    ```
3.  **Akses Web**:
    Buka peramban (browser) dan ketik alamat: `http://127.0.0.1:5000/`

## 5. Metadata Pengembangan
- **Framework**: Flask
- **Algoritma Utama**: Decision Tree Classifier
- **Library Utama**: Scikit-Learn, Pandas, NumPy, Joblib

---
*Dibuat untuk keperluan dokumentasi teknis pengembangan sistem prediksi berbasis data.*
