# Menghapus kolom 'Usia'
df = df.drop(columns='Usia')
print(df)

# Menambah baris baru
new_row = {'Nama': 'Alice', 'Kota': 'Los Angeles', 'Pekerjaan': 'Pengacara'}
df = df.append(new_row, ignore_index=True)
print(df)

# Mengganti nama kolom 'Pekerjaan' menjadi 'Profesi'
df = df.rename(columns={'Pekerjaan': 'Profesi'})
print(df)

# Mengambil data berdasarkan indeks
subset = df.loc[1:2, ['Nama', 'Kota']]
print(subset)

# Menambahkan kolom 'Gaji'
df['Gaji'] = df['Usia'] * 1000
print(df)

# Mengelompokkan berdasarkan 'Kota' dan menghitung rata-rata usia
grouped_data = df.groupby('Kota')['Usia'].mean().reset_index()
print(grouped_data)

# Membuat DataFrame kedua
data2 = [
    ['John', 'CEO'],
    ['Jane', 'Data Scientist'],
    ['Bob', 'Designer']
]

columns2 = ['Nama', 'Posisi']
df2 = pd.DataFrame(data2, columns=columns2)
# Menggabungkan dua DataFrame berdasarkan kolom 'Nama'
merged_df = pd.merge(df, df2, on='Nama')
print(merged_df)

# Menyimpan DataFrame ke file CSV
df.to_csv('dataframe_example.csv', index=False)

