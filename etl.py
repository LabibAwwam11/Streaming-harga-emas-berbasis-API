import pandas as pd
import os

# Fungsi untuk mengubah harga emas menjadi 1 digit di belakang koma
def transform_price(price):
    if price is not None:
        # Mengubah harga emas menjadi 1 digit di belakang koma
        return round(price, 1)
    return None

# Fungsi untuk membaca data dari file CSV dan melakukan transformasi harga
def etl_from_csv(input_file="gold_price_data.csv", output_file="gold_price_data_transformed.csv"):
    try:
        # Periksa apakah file input ada
        if not os.path.exists(input_file):
            print(f"File {input_file} tidak ditemukan. Pastikan file tersebut ada di direktori yang benar.")
            return
        
        # Membaca data dari file CSV
        df = pd.read_csv(input_file)

        # Menampilkan data awal untuk verifikasi
        print(f"Data awal:\n{df.head()}")

        # Periksa apakah ada kolom harga (price)
        if 'price' in df.columns:
            # Transformasi harga emas menjadi 1 digit di belakang koma
            df['price'] = df['price'].apply(lambda x: round(x, 1) if isinstance(x, (int, float)) else x)

            # Menyimpan data yang sudah diubah ke dalam file CSV baru (dengan mode 'w' untuk memastikan file ditulis ulang)
            df.to_csv(output_file, index=False)
            print(f"Data berhasil disimpan dalam file {output_file}.")
        else:
            print("Kolom 'price' tidak ditemukan dalam data CSV.")
    
    except Exception as e:
        print(f"Terjadi kesalahan saat memproses data: {e}")

    # Menampilkan data yang telah diubah, dengan format 1 digit di belakang koma
    pd.set_option('display.float_format', '{:,.1f}'.format)  # Mengatur format tampilan untuk angka float
    print("\nData setelah transformasi:\n")
    print(df.head())

if __name__ == "__main__":
    # Proses ETL dari file CSV
    etl_from_csv()
