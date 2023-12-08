import pandas as pd

# Membuat Timestamp dari string
tanggal = pd.Timestamp('2023-01-01')

# Menampilkan hasil
print(tanggal)
#output : 2023-01-01 00:00:00

# Membuat DataFrame dengan DatetimeIndex
df = pd.DataFrame({'Nilai': [10, 20, 30]}, index=pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']))

# Menampilkan DataFrame
print(df)
# output
#             Nilai
# 2023-01-01     10
# 2023-01-02     20
# 2023-01-03     30

# Mengubah objek menjadi Timestamp atau DatetimeIndex
date_str = '2023-01-01'
tanggal = pd.to_datetime(date_str)

# Operasi Aritmatika Waktu
tanggal = pd.Timestamp('2023-01-01')
tanggal_tambah_satu_hari = tanggal + pd.Timedelta(days=1)

# Resampling ke mingguan
df_mingguan = df.resample('W').mean()

# Shifting data waktu
df_shifted = df.shift(periods=1)

# Ekstraksi informasi waktu
df['Tahun'] = df.index.year
df['Bulan'] = df.index.month

# Membaca data CSV dengan parsing kolom tanggal
df_csv = pd.read_csv('data.csv', parse_dates=['Tanggal'])

