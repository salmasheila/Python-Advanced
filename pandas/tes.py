
import pandas as pd

# Membuat Series dari list
data_list = [1, 2, 3, 4, 5]
series_from_list = pd.Series(data_list)

# Membuat Series dari tuple
data_tuple = (1, 2, 3, 4, 5)
series_from_tuple = pd.Series(data_tuple)

# Membuat Series dari dictionary
data_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
series_from_dict = pd.Series(data_dict)

# Menampilkan Series
print("Series from List:")
print(series_from_list)

print("\nSeries from Tuple:")
print(series_from_tuple)

print("\nSeries from Dictionary:")
print(series_from_dict)
