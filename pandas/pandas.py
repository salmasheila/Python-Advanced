import pandas as pd

# Contoh data list
data_list = [
    ['John', 25, 'New York'],
    ['Jane', 30, 'San Francisco'],
    ['Bob', 22, 'Chicago']
]

# Membuat DataFrame dari list
df_list = pd.DataFrame(data_list, columns=['Nama', 'Usia', 'Kota'])

# Menampilkan DataFrame
print(df_list)

import pandas as pd

# Contoh data dictionary
data_dict = {
    'Nama': ['John', 'Jane', 'Bob'],
    'Usia': [25, 30, 22],
    'Kota': ['New York', 'San Francisco', 'Chicago']
}

# Membuat DataFrame dari dictionary
df_dict = pd.DataFrame(data_dict)

# Menampilkan DataFrame
print(df_dict)

import pandas as pd

# Contoh data tuple list
data_tuples = [
    ('John', 25, 'New York'),
    ('Jane', 30, 'San Francisco'),
    ('Bob', 22, 'Chicago')
]

# Membuat DataFrame dari tuple list
df_tuples = pd.DataFrame(data_tuples, columns=['Nama', 'Usia', 'Kota'])

# Menampilkan DataFrame
print(df_tuples)


import pandas as pd

# Membaca data dari file CSV
df_csv = pd.read_csv('nama_file.csv')

# Menampilkan DataFrame dari file CSV
print(df_csv)
