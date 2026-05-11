import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("genz.csv")

print(df.head())

print(df.columns)

df = df.drop_duplicates()

print(df.isnull().sum())

df = df.fillna(0)

print(df[df["daily_usage_hours"] > 5])

print(df.sort_values("daily_usage_hours", ascending=False))

print(df.groupby("primary_platform")["daily_usage_hours"].mean())

df.groupby("primary_platform")["daily_usage_hours"].mean().plot(kind="bar")

plt.title("Average Daily Usage by Platform")

plt.xlabel("Platform")

plt.ylabel("Daily Usage Hours")

plt.show()

df.to_csv("cleaned_genz.csv", index=False)

print("Cleaning complete!")
