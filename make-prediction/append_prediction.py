# %%
import numpy as np
import pandas as pd
import os
from IPython.display import display
df = pd.read_csv('BII_History.csv', parse_dates=['<DTYYYYMMDD>'])
df_new = pd.read_csv('BII_Prediction.csv', parse_dates=['<DTYYYYMMDD>'])


df_merge = pd.concat([df, df_new[0:1]])
df_merge.sort_values(by=['<DTYYYYMMDD>'], inplace=True)
df_merge.drop_duplicates(subset ='<DTYYYYMMDD>', 
                     keep = "last", inplace = True) 
df_merge.to_csv('BII_MERGE.csv')
# %%
