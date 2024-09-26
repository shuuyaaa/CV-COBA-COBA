from datetime import datetime, timedelta

def tanggal_sebelumnya(tanggal_str, bulan_str, tahun_str):
    try:
        # Mengonversi input menjadi integer
        tanggal = int(tanggal_str)
        bulan = int(bulan_str)
        tahun = int(tahun_str)

        # Membuat objek tanggal
        tgl = datetime(tahun, bulan, tanggal)

        # Menghitung tanggal sebelumnya
        tgl_sebelumnya = tgl - timedelta(days=1)

        # Mengambil hari, bulan, dan tahun dari tanggal sebelumnya
        hari_sebelumnya = tgl_sebelumnya.day
        bulan_sebelumnya = tgl_sebelumnya.month
        tahun_sebelumnya = tgl_sebelumnya.year

        return hari_sebelumnya, bulan_sebelumnya, tahun_sebelumnya
    except ValueError as e:
        return str(e)

# Input dari pengguna
tanggal_str = input("Masukkan hari (1-31): ")
bulan_str = input("Masukkan bulan (1-12): ")
tahun_str = input("Masukkan tahun (misal: 2024): ")

# Mendapatkan tanggal sebelumnya
hari_sebelumnya, bulan_sebelumnya, tahun_sebelumnya = tanggal_sebelumnya(tanggal_str, bulan_str, tahun_str)

# Menampilkan hasil
if isinstance(hari_sebelumnya, int):  # Memeriksa apakah hasilnya adalah tanggal yang valid
    print(f"Tanggal satu hari sebelum {tanggal_str}/{bulan_str}/{tahun_str} adalah {hari_sebelumnya}/{bulan_sebelumnya}/{tahun_sebelumnya}.")
else:
    print(f"Kesalahan: {hari_sebelumnya}")
