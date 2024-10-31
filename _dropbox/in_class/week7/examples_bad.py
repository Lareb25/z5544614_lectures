""" Utils to create example DFs and series

BAD VERSION

Usage
-----

Can be called from other modules:

    from in_class.week7 import examples_bad


Notes
-----

The problem with this version is that it is defining objects at the module
level which are meant to be imported by other modules.

This version is not ideal for a number of reasons:

1.  We are creating constants at the module level and modifying them later in
    the code. Constants should not be modified at runtime!

2.  Since the series are defined at the module level, they are created ONLY
    ONCE when this module is imported. If another module modifies them by
    mistake, it will affect any further references (see example below).


Example: Sorting a copy of `ser_unsorted`

Start by importing this module:

from in_class.week7 import examples_bad as eg
print(eg.ser_unsorted)
2020-01-03    7.19  
2020-01-02    7.16
2020-01-06    7.00
2020-01-07    7.10
2020-01-08    6.86
2020-01-09    6.95
2020-01-10    7.00
2020-01-13    7.02
2020-01-14    7.11
2020-01-15    7.04

The following will first create a copy of `eg.ser_unsorted` and then sort that
copy (not the series assigned to eg.ser_unsorted`

ser0 = eg.ser_unsorted.copy()       # Deep copy of series
ser0.sort_index(inplace=True)
print(eg.ser_unsorted)              # eg.ser_unsorted is NOT SORTED
2020-01-03    7.19  
2020-01-02    7.16
2020-01-06    7.00
2020-01-07    7.10
2020-01-08    6.86
2020-01-09    6.95
2020-01-10    7.00
2020-01-13    7.02
2020-01-14    7.11
2020-01-15    7.04

This worked because we did not modify the original series assigned to
`eg.ser_unsorted`.

Suppose we forget to create a copy:

ser0 = eg.ser_unsorted
ser0.sort_index(inplace=True)
print(eg.ser_unsorted)              # eg.ser_unsorted is SORTED!
2020-01-02    7.16
2020-01-03    7.19  
2020-01-06    7.00
2020-01-07    7.10
2020-01-08    6.86
2020-01-09    6.95
2020-01-10    7.00
2020-01-13    7.02
2020-01-14    7.11
2020-01-15    7.04

The problem with the statements above is that we did NOT create a new series.
Instead, the SAME series is assigned to both `eg.ser_unsorted` and
`ser0`


Bottom line: Instead of having to copy the series created by this module,
create a function which will always return a new series. See
`examples.py` for one implementation

In general, always use functions if your goal is to create objects which are
meant to be used (and possibly modified) by other modules.

         
"""

import pandas as pd


# ----------------------------------------------------------------------------
#   The dates and prices lists (sorted)
# ----------------------------------------------------------------------------
DATES = [
    '2020-01-02',       # <- Sorted
    '2020-01-03',       # <- Sorted
    '2020-01-06',
    '2020-01-07',
    '2020-01-08',
    '2020-01-09',
    '2020-01-10',
    '2020-01-13',
    '2020-01-14',
    '2020-01-15',
]

PRICES = [
    7.1600,             # <- Price on 2020-02-02
    7.1900,             # <- Price on 2020-02-03
    7.0000,
    7.1000,
    6.8600,
    6.9500,
    7.0000,
    7.0200,
    7.1100,
    7.0400,
]

# Create a sorted version of the series
# 2020-01-02    7.16    <- SORTED
# 2020-01-03    7.19    <- SORTED
# 2020-01-06    7.00
# 2020-01-07    7.10
# 2020-01-08    6.86
# 2020-01-09    6.95
# 2020-01-10    7.00
# 2020-01-13    7.02
# 2020-01-14    7.11
# 2020-01-15    7.04
ser = pd.Series(data=PRICES, index=DATES)


# Create an unsorted version of the example series
#
# 2020-01-03    7.19    <- NOT SORTED
# 2020-01-02    7.16    <- NOT SORTED
# 2020-01-06    7.00
# 2020-01-07    7.10
# 2020-01-08    6.86
# 2020-01-09    6.95
# 2020-01-10    7.00
# 2020-01-13    7.02
# 2020-01-14    7.11
# 2020-01-15    7.04

# Swap the first and second elements:
DATES[1], DATES[0] = DATES[0], DATES[1]
PRICES[1], PRICES[0] = PRICES[0], PRICES[1]
ser_unsorted = pd.Series(data=PRICES, index=DATES)

# NOTE: The tuple unpacking above is modifying CONSTANTS!
# This is VERY bad practice. Instead, we should create copies first:
#
#   dates, prices = list(DATES), list(PRICES)
#
# Now modify the copies
#
#   dates[1], dates[0] = dates[0], dates[1]
#   prices[1], prices[0] = prices[0], prices[1]
# 
# Then create the series as follows:
#
#   ser_unsorted = pd.Series(data=prices, index=dates)



def _test():
    """ <++>
    """
    line_sep = '-' * 40

    print(
            line_sep,
            'This is ser:',
            '',
            ser,
            line_sep,
            sep='\n',
            )

    print(
            line_sep,
            'This is ser_unsorted:',
            '',
            ser_unsorted,
            line_sep,
            sep='\n',
            )
    

# ---------------------------------------------------------------------------- 
#   test
# ---------------------------------------------------------------------------- 
if __name__ == "__main__":
    _test()
    





