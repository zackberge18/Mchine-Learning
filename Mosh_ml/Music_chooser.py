import pandas as pd

data=pd.read_csv("music.csv")

print(data.drop(columns=["genre"]))

