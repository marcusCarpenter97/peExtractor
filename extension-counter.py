import pandas as pd

df_nine = pd.read_csv("extensions00389.csv", header=None)
df_eight = pd.read_csv("extensions00388.csv", header=None)

print("389")
print(df_nine.groupby([1]).count().to_csv("ecount389.csv"))
print("388")
print(df_eight.groupby([1]).count().to_csv("ecount388.csv"))

