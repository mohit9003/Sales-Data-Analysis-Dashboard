import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("sales.csv")

# show first rows
print(df.head())

# convert date
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

# total sales
print("Total Sales:", df["Sales"].sum())

# category sales
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)

# top cities
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)
print(city_sales.head(5))

# monthly sales
df["Month"] = df["Order Date"].dt.month
monthly_sales = df.groupby("Month")["Sales"].sum()

# graphs
category_sales.plot(kind="bar", title="Sales by Category")
plt.show()

monthly_sales.plot(title="Monthly Sales Trend")
plt.show()

category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.show()


df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)