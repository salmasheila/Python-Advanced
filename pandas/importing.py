import pandas as pd

# Mengimpor data dari file CSV
df_csv = pd.read_csv('contoh_data.csv')

# Mengimpor data dari file Excel
df_excel = pd.read_excel('contoh_data.xlsx', sheet_name='Sheet1')

# Mengimpor data dari clipboard (copy-paste)
df_clipboard = pd.read_clipboard()

url = 'https://example.com/data.csv'
df_url = pd.read_csv(url)

import sqlite3
# Membuat koneksi ke database SQLite
conn = sqlite3.connect('database.db')

# Mengimpor data dari tabel SQL ke dalam DataFrame
query = 'SELECT * FROM nama_tabel'
df_sql = pd.read_sql(query, conn)

# Menampilkan lima baris pertama dari DataFrame
print(df_sql.head())

# Menutup koneksi
conn.close()


