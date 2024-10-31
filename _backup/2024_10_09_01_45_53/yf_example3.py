"""
Module Name: yf_example3
Purpose: Download Qantas stock prices for a given year and save it in a CSV file.
"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year: int):
    """
    Download Qantas stock prices for a given year into a CSV file.

    :param year: The year for which to download the stock prices.
    """

    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    ticker_symbol = 'QAN.AX'

    filename = f"qan_prc_{year}.csv"
    file_path = os.path.join(cfg.DATADIR, filename)

    yf_example2.yf_prc_to_csv(tic=ticker_symbol, pth=file_path, start=start_date, end=end_date)

if __name__ == "__main__":
    qan_prc_to_csv(year=2020)
