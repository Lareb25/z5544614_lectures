""" lec_pd_series.py

Companion codes for the lecture on pandas Series
"""

import pandas as pd

# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
dates = [
    '2020-01-02',
    '2020-01-03',
    '2020-01-06',
    '2020-01-07',
    '2020-01-08',
    '2020-01-09',
    '2020-01-10',
    '2020-01-13',
    '2020-01-14',
    '2020-01-15',
]

prices = [
    7.1600,
    7.1900,
    7.0000,
    7.1000,
    6.8600,
    6.9500,
    7.0000,
    7.0200,
    7.1100,
    7.0400,
]

# ----------------------------------------------------------------------------
#   Create a Series instance
# ----------------------------------------------------------------------------
# Create a series object
ser = pd.Series(data=prices, index=dates)
print(ser)

# Accessing specific prices using the `prices` list and the `ser` series
# Select Qantas price on '2020-01-02' ($7.16) using ...
# Using the `prices` list
prc0 = prices[dates.index('2020-01-02')]
print(prc0)  # Output: 7.16

# Using the `ser` series
prc1 = ser['2020-01-02']
print(prc1)  # Output: 7.16

# ----------------------------------------------------------------------------
#   Slicing series
# ----------------------------------------------------------------------------
# Unlike dictionaries, you can slice a series
prcs = ser['2020-01-06':'2020-01-10']
print(prcs)

# Output:
#  2020-01-06    7.00
#  2020-01-07    7.10
#  2020-01-08    6.86
#  2020-01-09    6.95
#  2020-01-10    7.00
#  dtype: float64

# ----------------------------------------------------------------------------
#   Accessing the underlying array
# ----------------------------------------------------------------------------
# Use `.array` to get the underlying data array
ary = ser.array
print(ary)

# Use the `index` attribute to get the index from a series
the_index = ser.index
print(the_index)

# Changing the index by assignment
ser.index = [0, 1, 2, 3, -4, 5, 6, 7, 8, 1000]
print(ser)

# Selecting observations using the new index
# This will return 7.04
x = ser[1000]
print(x)  # Output: 7.04

# Compare accessing using the new index vs. list
# This will return the element associated with the index label -4
print(ser[-4])  # Output: 6.86

# This will return the fourth element from the end of the list `prices`
print(prices[-4])  # Output: 7.00
