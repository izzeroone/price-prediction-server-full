# %%
import pandas as pd
import pandas_market_calendars as mcal
from IPython.display import display
import numpy as np
df_org = pd.read_csv('data/khd.csv', parse_dates=['<DTYYYYMMDD>'])
df_org = df_org.sort_values('<DTYYYYMMDD>')
df_org = df_org.set_index('<DTYYYYMMDD>')
df_org = df_org.tz_localize(None)

stock_calendar = mcal.get_calendar('stock')
stock_time = stock_calendar.valid_days(start_date=df_org.index.values[0], end_date=df_org.index.values[-1])
stock_time.tz_localize(None)
df_time = pd.DataFrame((stock_time), columns=['<DTYYYYMMDD>'])
df_time = df_time.sort_values('<DTYYYYMMDD>')
df_time = df_time.set_index('<DTYYYYMMDD>')
df_time = df_time.tz_convert(None)

df_org = df_org.join(df_time, how='right')

df_org = df_org.reset_index()
df_org = df_org.fillna(method='backfill')
display(df_org.head(10))

# %%
