import yfinance as yf

def yf_prc_to_csv(tic, pth, start=None, end=None):
    df = yf.download(tic, start=start, end=end, ignore_tz=True)
    df.to_csv(pth)