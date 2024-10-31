""" Utils to create example DFs and series

This is an improved version of examples_bad.py

Usage
-----

Can be called from other modules:

from in_class.week7 import examples


Notes
-----

This module modifies examples_bad.py as follows:

1.  Instead of defining functions at the module level, delegate this task to a
    function called `mk_data`. This function will create NEW lists every time we
    call it.

2.  Similarly, the series are NOT created at the module level. Instead, this
    task is delegated to the functions `mk_ser` and `mk_ser_unsorted`.  These
    functions return NEW series when called.

3.  This module includes a new function, `mk_df`, which creates an example DF

         
"""

import pandas as pd


# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
def mk_data() -> tuple:
    """ Returns a tuple with lists of dates, prices, and trading days

    Returns
    -------
    tuple:
        (dates, prices, bday)
        

    Notes
    -----
    Note that this function always returns NEW lists
    """

    dates = [
        '2020-01-02',       # <- SORTED
        '2020-01-03',       # <- SORTED
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
    # Trading day counter
    bday = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10]
    return (dates, prices, bday)


def mk_ser():
    """ Returns an example series

    Returns
    -------
    series: 
        A series with elements:

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

    """
    dates, prices, bday = mk_data()
    return pd.Series(data=prices, index=dates)

def mk_ser_unsorted():
    """ Returns a modified version of the example series, in which the first
    two obs are swapped

    Returns
    -------
    series: 
        A series with elements:

        2020-01-03    7.19  <- Not sorted
        2020-01-02    7.16  <- Not sorted
        2020-01-06    7.00
        2020-01-07    7.10
        2020-01-08    6.86
        2020-01-09    6.95
        2020-01-10    7.00
        2020-01-13    7.02
        2020-01-14    7.11
        2020-01-15    7.04


    """
    dates, prices, bday = mk_data()
    dates[1], dates[0] = dates[0], dates[1]
    prices[1], prices[0] = prices[0], prices[1]
    return pd.Series(data=prices, index=dates)


def mk_df():
    """ Returns an example DF with elements:

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

    """
    dates, prices, bday = mk_data()
    data = {
            'Close': prices,
            'Bday': bday,
            }
    return pd.DataFrame(data=data, index=dates)


def _test():
    """ Test function
    """
    # Separator
    line_sep = '-' * 40

    # Create the default series
    ser = mk_ser()
    print(
            line_sep,
            "mk_ser() -> ", 
            '',
            ser,
            line_sep,
            '',
            sep='\n')

    # Create unsorted series
    ser = mk_ser_unsorted()
    print(
            line_sep,
            "mk_ser_unsorted() -> ", 
            '',
            ser,
            line_sep,
            '',
            sep='\n')

    # Create the default DF
    df = mk_df()
    print(
            line_sep,
            "mk_df() -> ", 
            '',
            df,
            line_sep,
            '',
            sep='\n')
    

# ---------------------------------------------------------------------------- 
#   test
# ---------------------------------------------------------------------------- 
if __name__ == "__main__":
    _test()
    





