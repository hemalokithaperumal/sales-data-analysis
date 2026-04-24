import pandas as pd
import matplotlib.pyplot as plt
# load dataset
data = pd.read_csv("sales_data.csv")
print(data.head())  # see first 5 rows
#adding total
data["Total"] = data["Quantity"] * data["Price"]
print(data)
total_sales = data["Total"].sum()
print("Total Sales:", total_sales)

best_product = data.groupby("Product")["Quantity"].sum().idxmax()
print("Best Selling Product:", best_product)


city_sales = data.groupby("City")["Total"].sum()
print("\nSales by City:\n", city_sales)


data["Date"] = pd.to_datetime(data["Date"], format="%d-%m-%Y")
data["Month"] = data["Date"].dt.month

monthly_sales = data.groupby("Month")["Total"].sum()
print("\nMonthly Sales:\n", monthly_sales)




monthly_sales.plot(kind='bar')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


top_city = city_sales.idxmax()
print("Top Performing City:", top_city)

monthly_sales.to_csv("monthly_sales.csv")
city_sales.to_csv("city_sales.csv")

city_sales.plot(kind='bar')
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

sorted_products = data.groupby("Product")["Total"].sum().sort_values(ascending=False)
print("\nProduct Performance:\n", sorted_products)
