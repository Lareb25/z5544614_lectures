import pandas as pd

# The dates and prices lists
dates = [
    '2020-01-02', '2020-01-03', '2020-01-06',
    '2020-01-07', '2020-01-08', '2020-01-09',
    '2020-01-10', '2020-01-13', '2020-01-14',
    '2020-01-15'
]

prices = [
    7.1600, 7.1900, 7.0000,
    7.1000, 6.8600, 6.9500,
    7.0000, 7.0200, 7.1100,
    7.0400
]

bday = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create two series
prc_ser = pd.Series(data=prices, index=dates)  # Series with prices
bday_ser = pd.Series(data=bday, index=dates)    # Series with trading day

# Create a DataFrame using the series
df = pd.DataFrame({'Close': prc_ser, 'Bday': bday_ser})
print(df)

# Accessing the indexes in a dataframe
print("Column Index:", df.columns)
print("Row Index:", df.index)

# Accessing a specific column as a Series
col0 = df['Close']
print("Close Series:\n", col0)

# Modify columns and indexes
df.columns = ['A', 'B']  # Rename columns
df.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Rename indexes
print("Modified DataFrame:\n", df)

# Revert back to original column names and indexes
df.columns = ['Close', 'Bday']
df.index = [
    '2020-01-02', '2020-01-03', '2020-01-06',
    '2020-01-07', '2020-01-08', '2020-01-09',
    '2020-01-10', '2020-01-13', '2020-01-14',
    '2020-01-15'
]
print("Reverted DataFrame:\n", df)

# Create a series with an unsorted index
new_ser = pd.Series(data=[1, 3, 2], index=['a', 'c', 'b'])
print("Unsorted Series:\n", new_ser)

# Sort the series based on the index
sorted_ser = new_ser.sort_index()
print("Sorted Series:\n", sorted_ser)

# Slicing sorted series
x = sorted_ser['a':'b']  # This will return the intersection between the slice and the row labels
print("Sliced Series:\n", x)

# Sort the DataFrame by index
df_sorted = df.sort_index()
print("Sorted DataFrame:\n", df_sorted)
