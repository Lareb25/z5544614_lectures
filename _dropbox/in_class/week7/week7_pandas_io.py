""" In-class companion codes for Week 7 (pandas IO)

         
"""

import os

import pandas as pd

import toolkit_config as cfg
from in_class.week7 import utils


# Variables with the location of the following files
# toolkit/
# |__ data/
# |   |__ qan_prc_2020.csv           
# |   |__ qan_prc_with_index.csv     
# |   |__ qan_prc_no_index.csv      

QAN_PRC_CSV = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
QAN_WITHINDEX_CSV = os.path.join(cfg.DATADIR, 'qan_prc_with_index.csv')
QAN_NOINDEX_CSV = os.path.join(cfg.DATADIR, 'qan_prc_no_index.csv')


def printit(*args, 
            add_sep = False,
            show_type = False,
            show_id = False,
            ):
    """ Run utils.printit function with other defaults
    """
    utils.printit(*args, add_sep=add_sep, show_type=show_type, show_id=show_id)


def example1():
    """ Reading data from a CSV file
    """
    printit("Running example1()")

    # Alternative 1:
    #
    # Load the data contained in qan_prc_2020.csv to a DF
    # and then set the index using the .set_index method
    df = pd.read_csv(QAN_PRC_CSV)
    df.set_index('Date', inplace=True)
    printit(
            'Alternative 1:',
            'df = pd.read_csv(QAN_PRC_CSV)',
            "df.set_index('Date', inplace=True)",
            'Then df is:',
            df,
            )

    # Alternative 2: use the index_col parameter
    df = pd.read_csv(QAN_PRC_CSV, index_col='Date')
    printit(
            'Alternative 2: Use the index_col parm',
            "df = pd.read_csv(QAN_PRC_CSV, index_col='Date')",
            'Then df is:',
            df,
            )



def example2():
    """ Storing data to a CSV file
    """

    # First, we read the data into a dataframe (without setting the index)
    # Then save it using he .to_csv method
    df = pd.read_csv(QAN_PRC_CSV)

    # By default, pandas will include the index in the file
    df.to_csv(QAN_WITHINDEX_CSV)

    # You can exclude the index by setting the parm index to False
    df.to_csv(QAN_NOINDEX_CSV, index=False)


def main():
    """
    """
    examples_to_run = [
            #example1,
            #example2,
            ]

    #  run examples
    for func in examples_to_run:
        func()

if __name__ == "__main__":
    main()

