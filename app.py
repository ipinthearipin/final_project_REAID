import streamlit as st
import pandas as pd
import numpy as np
from huggingface_hub import hf_hub_download
from joblib import load

# --- Kelas dan Fungsi ---
class PengeluaranHarian:
    def __init__(self, hari, makanan, transportasi, belanja, lainnya):
        self.hari = hari
        self.makanan = makanan
        self.transportasi = transportasi
        self.belanja = belanja
        self.lainnya = lainnya

    def to_dict(self):
        return {
            "day": self.hari,
            "food": self.makanan,
            "transport": self.transportasi,
            "shopping": self.belanja,
            "others": self.lainnya
        }

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="Prediksi Pengeluaran Bulanan", page_icon="💰", layout="centered")
st.markdown("""
    <style>
        .main {background-color: #f9f9f9;}
        .block-container {padding-top: 2rem;}
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 0.5rem;
            height: 3em;
        }
        .stDataFrame {background-color: white; border-radius: 0.5rem;}
    </style>
""", unsafe_allow_html=True)

# --- Inisialisasi Session State ---
if "daily_data" not in st.session_state:
    st.session_state.daily_data = []

# --- Sidebar ---
st.sidebar.title("⚙️ Pengaturan")
st.sidebar.markdown("Masukkan pengaturan anggaran bulanan Anda")
budget = st.sidebar.number_input("💰 Anggaran Bulanan (Rp)", min_value=0, value=1000000, step=50000)

if st.sidebar.button("🔄 Reset Semua Data"):
    st.session_state.daily_data = []
    st.success("✅ Data berhasil direset!")

st.sidebar.markdown("""
---
### ℹ️ Tentang Aplikasi
Aplikasi ini membantu Anda memantau pengeluaran harian dan memprediksi total pengeluaran bulanan menggunakan model AI berbasis regresi.

✅ Input harian: Makanan, Transportasi, Belanja, dan Lainnya  
✅ Rata-rata dihitung otomatis  
✅ Model dipanggil langsung dari Hugging Face

Dikembangkan oleh: 
                    
    Muhammad Faza Arifin 
    REAPYTHON3QDCBL

---
""")

# --- Judul Utama ---
st.title("📊 Prediksi AI Pengeluaran Bulanan")
st.markdown("Masukkan pengeluaran harian Anda dan biarkan AI memprediksi total pengeluaran bulanan Anda.")

# --- Form Input Harian ---
st.subheader("📝 Input Pengeluaran Harian")
with st.form("daily_form"):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        day = st.number_input("Hari", min_value=1, max_value=31, value=1, step=1)
    with col2:
        food = st.number_input("Makanan", min_value=0, value=0, step=500)
    with col3:
        transport = st.number_input("Transportasi", min_value=0, value=0, step=500)
    with col4:
        shopping = st.number_input("Belanja", min_value=0, value=0, step=500)
    with col5:
        others = st.number_input("Lainnya", min_value=0, value=0, step=500)

    submitted = st.form_submit_button("➕ Tambah Data")
    if submitted:
        entry = PengeluaranHarian(day, food, transport, shopping, others)
        st.session_state.daily_data.append(entry.to_dict())
        st.success("✅ Data berhasil ditambahkan!")

# --- Tampilkan Tabel ---
if st.session_state.daily_data:
    df = pd.DataFrame(st.session_state.daily_data)
    st.subheader("📅 Ringkasan Data Harian")
    st.dataframe(df.sort_values(by="day"), use_container_width=True, height=300)

    # --- Feature Engineering ---
    avg_food = df['food'].mean()
    avg_transport = df['transport'].mean()
    avg_shopping = df['shopping'].mean()
    avg_others = df['others'].mean()

    # --- Prediksi ---
    st.subheader("📈 Prediksi Pengeluaran")
    if st.button("🔍 Prediksi Pengeluaran Bulanan"):
        try:
            HF_TOKEN = "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"  # Ganti dengan token kamu
            model_path = hf_hub_download(
                repo_id="ipinthearipin/monthly-expense-predictor",
                filename="monthly_expense_predictor_retrained.joblib",
                token=HF_TOKEN
            )
            model = load(model_path)

            input_data = np.array([[avg_food, avg_transport, avg_shopping, avg_others]])
            prediction = model.predict(input_data)[0]

            st.success(f"🎯 Prediksi Total Pengeluaran Bulanan: Rp{prediction:,.2f}")

            diff = budget - prediction
            if diff >= 0:
                st.info(f"💡 Anda bisa menghemat sekitar Rp{diff:,.2f} bulan ini!")
            else:
                st.warning(f"⚠️ Anda mungkin melebihi anggaran sebesar Rp{-diff:,.2f}. Pertimbangkan penghematan.")
        except Exception as e:
            st.error(f"❌ Gagal memuat model atau menghitung prediksi: {e}")
else:
    st.info("ℹ️ Tambahkan minimal satu data harian untuk memulai prediksi.")
