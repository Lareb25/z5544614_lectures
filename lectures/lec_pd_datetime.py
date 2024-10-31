""" lec_pd_datetime.py

Companion codes for the lecture on working with time-series data in Pandas
"""
import os
import datetime as dt

import pandas as pd

import toolkit_config as cfg
CSVLOC = os.path.join(cfg.DATADIR, 'tsla_prc.csv')

dt_now = dt.datetime.now()
print(dt_now)  # This prints the current date and time
print(type(dt_now))  # This confirms it is a datetime instance

s = 'Date in day/month/year format is: {}/{}/{}'.format(dt_now.day, dt_now.month, dt_now.year)
print(s)  # Expected output: Date in day/month/year format is: [day]/[month]/[year]

print(dt_now)  # Regular print of dt_now
print(repr(dt_now))  # Shows how the instance could be constructed

a_little_ago = dt.datetime(year=2021, month=8, day=21, hour=13, minute=24, second=27, microsecond=283311)
print(a_little_ago)

dt0 = dt.datetime(year=2019, month=12, day=31)
dt1 = dt.datetime(year=2020, month=1, day=1)
delta = dt1 - dt0
print(repr(delta))  # Expected output: datetime.timedelta(days=1)

prc = pd.read_csv(CSVLOC)
print(prc.head())

prc['Date'] = pd.to_datetime(prc['Date'], format='%Y-%m-%d')
print(prc.info())  # This should show the Date column as datetime64 type




import os
import pandas as pd

# Define CSV location
CSVLOC = os.path.join(cfg.DATADIR, 'tsla_prc.csv')

# Load the data into a DataFrame
prc = pd.read_csv(CSVLOC)
print(prc)

# Inspect data types
prc.info()

# Convert 'Date' column to datetime
prc['Date'] = pd.to_datetime(prc['Date'], format='%Y-%m-%d')
prc.info()

# Set the 'Date' column as the index
prc.set_index('Date', inplace=True)
prc.info()

# Check the new index
print(prc.index)




from datetime import datetime
birth_date = datetime(year=1999, month=9, day=8)
seconds_alive = (datetime.now() - birth_date).total_seconds()
print(f"You have been alive for {seconds_alive:.0f} seconds.")

from datetime import timedelta
future_date = datetime.now() + timedelta(days=1340)
future_age = future_date.year - birth_date.year - ((future_date.month, future_date.day) < (birth_date.month, birth_date.day))
print(f"You will be {future_age} years old in 1,340 days.")

print("Lareb Zaidi, z5544614")