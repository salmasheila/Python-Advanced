import pandas as pd

# Membuat Pandas Series
data_list = [10, 20, 30, 40, 50]
index_labels = ['a', 'b', 'c', 'd', 'e']
my_series = pd.Series(data_list, index=index_labels, name='MySeries')

# 1. Mengakses Nilai (values)
values = my_series.values
print("Values in the Series:", values)

# 2. Mengakses Indeks (index)
index_values = my_series.index
print("Index of the Series:", index_values)

# 3. Mengetahui Tipe Data (dtype)
data_type = my_series.dtype
print("Data Type of the Series:", data_type)

# 4. Mengetahui Nama (name)
series_name = my_series.name
print("Name of the Series:", series_name)

# 5. Mengetahui Bentuk (shape)
series_shape = my_series.shape
print("Shape of the Series:", series_shape)

# 6. Mengetahui Jumlah Elemen (size)
series_size = my_series.size
print("Size of the Series:", series_size)

# 7. Mengetahui Apakah Kosong atau Tidak (empty)
is_empty = my_series.empty
print("Is the Series Empty?", is_empty)
