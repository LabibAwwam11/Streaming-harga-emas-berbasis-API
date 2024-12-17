import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk membaca data dari file CSV
def load_data_from_csv(csv_file="gold_price_data_transformed.csv"):
    try:
        # Membaca data dari file CSV
        df = pd.read_csv(csv_file)

        # Pastikan kolom 'timestamp' dan 'price' ada dalam data
        if 'timestamp' in df.columns and 'price' in df.columns:
            return df['timestamp'], df['price']
        else:
            print("File CSV tidak memiliki kolom yang diperlukan.")
            return pd.Series(), pd.Series()  # Mengembalikan Series kosong
    except Exception as e:
        print(f"Error saat membaca file CSV: {e}")
        return pd.Series(), pd.Series()  # Mengembalikan Series kosong

# Fungsi untuk memperbarui grafik
def update_graph(times, prices):
    # Clear grafik sebelumnya dan plot data terbaru
    ax.clear()
    ax.plot(times, prices, marker='o', color='gold', linestyle='-', linewidth=2, markersize=5)
    ax.set_title('Harga Emas (XAU/USD) Seiring Waktu', fontsize=14)
    ax.set_xlabel('Waktu', fontsize=12)
    ax.set_ylabel('Harga Emas (USD)', fontsize=12)
    plt.xticks(rotation=45)
    ax.grid(True)

# Membaca data dari file CSV
times, prices = load_data_from_csv("gold_price_data_transformed.csv")

# Memeriksa apakah data ada
if not times.empty and not prices.empty:
    # Membuat figure dan axis untuk plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Menampilkan grafik dengan data yang sudah ada
    update_graph(times, prices)

    # Menampilkan grafik
    plt.tight_layout()
    plt.show()
else:
    print("Tidak ada data untuk ditampilkan.")
