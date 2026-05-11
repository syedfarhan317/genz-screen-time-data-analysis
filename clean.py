import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("genz.csv")

# Show first 5 rows
print(df.head())

# Show column names
print(df.columns)

# Remove duplicate rows
df = df.drop_duplicates()

# Check missing values
print(df.isnull().sum())

# Fill missing values with 0
df = df.fillna(0)

# Filter people using social media more than 5 hours daily
print(df[df["daily_usage_hours"] > 5])

# Sort highest daily usage first
print(df.sort_values("daily_usage_hours", ascending=False))

# Average daily usage by platform
print(df.groupby("primary_platform")["daily_usage_hours"].mean())

# Create bar chart
df.groupby("primary_platform")["daily_usage_hours"].mean().plot(kind="bar")

# Chart title
plt.title("Average Daily Usage by Platform")

# X-axis label
plt.xlabel("Platform")

# Y-axis label
plt.ylabel("Daily Usage Hours")

# Show chart
plt.show()

# Save cleaned file
df.to_csv("cleaned_genz.csv", index=False)

print("Cleaning complete!")