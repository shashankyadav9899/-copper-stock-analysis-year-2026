import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("copper stock analysis.csv")

print(df.shape)
df.head()
df.info()
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
df["Date"] = pd.to_datetime(df["Date"])
df = df[["Date","Ticker","Open","High","Low","Close","Volume"]]
df = df.drop_duplicates()
df = df.dropna()
df[["Open","High","Low","Close"]] = df[["Open","High","Low","Close"]].round(2)
df = df.sort_values(["Ticker","Date"]).reset_index(drop=True)

print(df.shape)
df.head()
g = df.groupby("Ticker")

df["MA4"]  = g["Close"].transform(lambda x: x.rolling(4).mean())
df["MA10"] = g["Close"].transform(lambda x: x.rolling(10).mean())
df["Weekly_Return_%"] = g["Close"].pct_change() * 100
df["Volatility_4w"] = df.groupby("Ticker")["Weekly_Return_%"].transform(lambda x: x.rolling(4).std())

df = df.round(2)
df.head(12)
summary = df.groupby("Ticker").agg(
    Highest_Price=("High","max"),
    Lowest_Price=("Low","min"),
    Avg_Weekly_Return=("Weekly_Return_%","mean"),
    Volatility=("Weekly_Return_%","std"),
    Avg_Volume=("Volume","mean")
).round(2)

first = g["Close"].first()
last  = g["Close"].last()
summary["Total_Return_%"] = ((last - first) / first * 100).round(2)

summary