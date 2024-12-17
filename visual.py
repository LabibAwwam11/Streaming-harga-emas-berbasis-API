import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import time

# Masukkan API Key Anda di sini
API_KEY = "goldapi-dv5sm4dh1bdw-io"

# Endpoint untuk mendapatkan harga XAU/USD
API_URL = "https://www.goldapi.io/api/XAU/USD"

# Header yang menyertakan API Key untuk autentikasi
HEADERS = {
    'x-access-token': API_KEY
}

# Data awal untuk grafik
times = []
prices = []

# Fungsi untuk mengambil harga emas dari API
def get_gold_price():
    try:
        response = requests.get(API_URL, headers=HEADERS, timeout=10)  # Timeout untuk menghindari hang
        response.raise_for_status()  # Periksa apakah HTTP request berhasil
        data = response.json()
        return data.get('price', None)
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil data: {e}")
        return None

# Fungsi untuk memperbarui grafik
def update(frame):
    # Ambil data harga emas terbaru
    price = get_gold_price()
    if price is not None:
        # Menambahkan data waktu dan harga ke list
        times.append(datetime.now().strftime('%H:%M:%S'))
        prices.append(price)

        # Membatasi jumlah data yang ditampilkan (misalnya hanya 30 titik terakhir)
        if len(times) > 30:
            times.pop(0)
            prices.pop(0)

        # Clear grafik sebelumnya dan plot data terbaru
        ax.clear()
        ax.plot(times, prices, marker='o', color='gold', linestyle='-', linewidth=2, markersize=5)
        ax.set_title('Harga Emas (XAU/USD) Seiring Waktu', fontsize=14)
        ax.set_xlabel('Waktu', fontsize=12)
        ax.set_ylabel('Harga Emas (USD)', fontsize=12)
        plt.xticks(rotation=45)
        ax.grid(True)

# Membuat figure dan axis untuk plot
fig, ax = plt.subplots(figsize=(10, 6))

# Membuat animasi untuk memperbarui grafik setiap 5 detik
ani = FuncAnimation(fig, update, interval=5000)  # interval dalam milidetik (5000ms = 5 detik)

# Menampilkan grafik secara real-time
plt.tight_layout()
plt.show()
