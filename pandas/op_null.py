import pandas as pd
import numpy as np

# Membuat DataFrame dengan nilai null
data = {'Nama': ['John', 'Jane', np.nan, 'Bob'],
        'Usia': [25, 30, np.nan, 22],
        'Kota': ['New York', 'San Francisco', 'Chicago', np.nan]}

df = pd.DataFrame(data)

print("DataFrame Awal:")
print(df)

# Mendeteksi lokasi nilai null
print("\nLokasi Nilai Null:")
print(df.isnull())

# Menghapus baris yang mengandung nilai null
df_cleaned_rows = df.dropna()
print("\nDataFrame setelah Menghapus Baris dengan Nilai Null:")
print(df_cleaned_rows)

# Mengganti nilai null dengan nilai tertentu
df_filled_value = df.fillna('Tidak Tersedia')
print("\nDataFrame setelah Mengganti Nilai Null:")
print(df_filled_value)

# Mengisi nilai null dengan interpolasi
df_interpolated = df.interpolate()
print("\nDataFrame setelah Interpolasi:")
print(df_interpolated)

# Mengganti nilai tertentu dengan nilai lain
df_replaced = df.replace(np.nan, 'Tidak Tersedia')
print("\nDataFrame setelah Mengganti Nilai:")
print(df_replaced)
