import requests
import json
import pandas as pd
import time
from datetime import datetime

# Masukkan API Key Anda di sini
API_KEY = "goldapi-dv5sm4dh1bdw-io"

# Endpoint untuk mendapatkan harga XAU/USD
API_URL = "https://www.goldapi.io/api/XAU/USD"

# Header yang menyertakan API Key untuk autentikasi
HEADERS = {
    'x-access-token': API_KEY
}

# Fungsi untuk mengambil harga emas dari API dan menyimpannya dalam file JSON
def get_and_save_gold_price_json():
    try:
        response = requests.get(API_URL, headers=HEADERS, timeout=10)  # Timeout untuk menghindari hang
        response.raise_for_status()  # Periksa apakah HTTP request berhasil
        data = response.json()

        # Menyimpan data dalam file JSON
        with open("gold_price_data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        print("Data berhasil disimpan dalam file JSON.")
    except requests.exceptions.Timeout:
        print("Error: Permintaan ke API timeout. Periksa koneksi Anda.")
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil data: {e}")

# Fungsi untuk mengubah data JSON menjadi format tabular dan menyimpannya ke dalam file CSV
def json_to_csv():
    try:
        # Membaca data dari file JSON
        with open("gold_price_data.json", "r") as json_file:
            data = json.load(json_file)

        # Menampilkan data untuk verifikasi
        print(f"Data JSON yang diambil: {data}")

        # Transformasi data JSON menjadi format tabular (pandas DataFrame)
        price = data.get("price", None)
        if price is not None:
            # Menambahkan timestamp agar setiap entri memiliki waktu
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            df = pd.DataFrame([{"timestamp": timestamp, "price": price}])  # Menyimpan data harga dalam tabular format

            # Menyimpan DataFrame ke file CSV dalam mode append
            df.to_csv("gold_price_data.csv", mode='a', header=not pd.io.common.file_exists("gold_price_data.csv"), index=False)
            print("Data berhasil disimpan dalam file CSV.")
        else:
            print("Tidak ada harga emas yang ditemukan dalam data.")
    except FileNotFoundError:
        print("File JSON tidak ditemukan. Pastikan Anda telah mengambil data terlebih dahulu.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengubah data ke CSV: {e}")

# Fungsi utama untuk melakukan streaming dan menyimpan data
def stream_and_save_data(interval=2):
    print("Memulai streaming dan penyimpanan harga emas...")
    try:
        while True:
            # Ambil data dari API dan simpan dalam file JSON
            get_and_save_gold_price_json()

            # Ubah data JSON menjadi CSV dan simpan
            json_to_csv()

            time.sleep(interval)  # Tunggu beberapa detik sebelum polling berikutnya
    except KeyboardInterrupt:
        print("\nStreaming dihentikan oleh pengguna.")

if __name__ == "__main__":
    stream_and_save_data()
