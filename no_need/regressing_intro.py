import pandas as pd
import quandl

df = quandl.get("WIKI/GOOGL")

print(df.head())

df=[["Adj. Open","Adj. High","Adj. Low","Adj. Close","Adj. Volume"]]