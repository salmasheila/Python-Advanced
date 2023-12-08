import pandas as pd

# Membuat DataFrame dengan kolom string
data = {'Nama': ['John', 'Jane', 'Bob'],
        'Kota': ['New York', 'San Francisco', 'Chicago']}
df = pd.DataFrame(data)

# Mengubah string menjadi lowercase
df['Nama_lower'] = df['Nama'].str.lower()

# Mengubah string menjadi uppercase
df['Kota_upper'] = df['Kota'].str.upper()

# Menambahkan kolom untuk panjang string
df['Panjang_Nama'] = df['Nama'].str.len()

# Menambahkan kolom untuk memotong string
df['Potongan_Kota'] = df['Kota'].str[:3]

# Menambahkan kolom untuk memisahkan string
df['Kota_Pisah'] = df['Kota'].str.split()

# Menambahkan kolom untuk menggabungkan string
df['Nama_Kota'] = df['Nama'] + ' di ' + df['Kota']

# Menambahkan kolom untuk mencari substring
df['Cari_NY'] = df['Kota'].str.contains('NY')

# Menambahkan kolom untuk mengganti string
df['Ganti_Francisco'] = df['Kota'].str.replace('Francisco', 'City')

# Menambahkan kolom untuk stripping (menghilangkan spasi di awal dan akhir)
df['Nama_Stripped'] = df['Nama'].str.strip()

# Menambahkan kolom untuk mengecek awalan dan akhiran string
df['Awalan_Bob'] = df['Nama'].str.startswith('Bob')
df['Akhiran_ohn'] = df['Nama'].str.endswith('ohn')

# Menambahkan kolom untuk mengubah tipe data string menjadi list
df['Nama_List'] = df['Nama'].str.split()










