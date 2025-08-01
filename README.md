# 💸 AI Prediksi Pengeluaran Bulanan

Aplikasi interaktif berbasis Python dan Streamlit untuk memantau pengeluaran harian dan memprediksi total pengeluaran bulanan menggunakan model Machine Learning.

---

## 🚀 Fitur

- ✏️ Input harian kategori: makanan, transportasi, belanja, lainnya
- 📊 Ringkasan pengeluaran harian dalam bentuk tabel
- 📈 Prediksi total pengeluaran bulanan berdasarkan rata-rata
- 💡 Saran penghematan dibandingkan anggaran
- 🔐 Input token Hugging Face pribadi langsung dari sidebar
- 🤖 Model AI terhubung ke Hugging Face

---

## 🧠 Model yang Digunakan

Model regresi linear sederhana yang dilatih menggunakan scikit-learn:

- **Fitur input:** `avg_food`, `avg_transport`, `avg_shopping`, `avg_others`
- **Output:** prediksi total pengeluaran bulanan
- **Target:** total_harian * 30

Model tersedia di Hugging Face:
👉 [ipinthearipin/monthly-expense-predictor](https://huggingface.co/ipinthearipin/monthly-expense-predictor)

---

## 🛠️ Teknologi

- Python
- Streamlit
- scikit-learn
- pandas
- numpy
- joblib
- huggingface_hub

---

## 📂 Struktur Direktori

```
📁 expense-predictor-app
├── app.py                   # Aplikasi utama Streamlit
├── README.md                # Dokumentasi
├── requirements.txt         # Daftar pustaka Python
├── docs/
│   └── tampilan_awal.png # Tampilan awal
│   └── hasil_prediksi.png # Hasil prediksi

```

---

## 📸 Cuplikan Tampilan

1. Tampilan awal
![screenshot](https://github.com/ipinthearipin/final_project_REAID/blob/main/docs/tampilan_awal.png)

2. Hasil prediksi
![screenshot](https://github.com/ipinthearipin/final_project_REAID/blob/main/docs/hasil_prediksi.png)

---

## ⚙️ Cara Menjalankan

1. Clone repositori ini

```bash
git clone https://github.com/ipinthearipin/final_project_REAID.git
cd final_project_REAID
```

2. Install dependency

```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi

```bash
streamlit run app.py
```

---

## 🔑 Token Hugging Face

Untuk mengakses model di Hugging Face, pengguna **harus memasukkan token mereka sendiri di sidebar** aplikasi.

- Token dapat diperoleh dari: https://huggingface.co/settings/tokens
- Pilih permission: `Read`

Token tidak disimpan di kode untuk menjaga keamanan.

---

## 📈 Contoh Prediksi

| Hari | Makanan | Transportasi | Belanja | Lainnya |
|------|---------|--------------|---------|---------|
| 1    | 20000   | 5000         | 8000    | 2000    |
| 2    | 25000   | 12000        | 9000    | 3000    |

Rata-rata digunakan untuk memprediksi total pengeluaran 30 hari.

---

## 🙋‍♂️ Developer

- 👨‍💻 [ipinthearipin](https://huggingface.co/ipinthearipin)
- 🤖 [Model AI di Hugging Face](https://huggingface.co/ipinthearipin/monthly-expense-predictor)

---

## 🪪 Lisensi

MIT License
