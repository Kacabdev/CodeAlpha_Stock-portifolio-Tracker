
import csv


stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

# getting user input
user_portifolio = {}

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Sorry, we don't have data for that stock. ")
        continue

    try:
        quantity = int(input(f"How many shares of {stock} do you own? "))
        if quantity < 0:
            print("Quantity can't be negative. ")
            continue

        user_portifolio[stock] = quantity
    except ValueError:
        print("Please enter a valid number for quantity")


#showing investment breakdown
total_value = 0
print("\n --- portifolio Breakdown ---")
print(f"{'Stock': <10}{'Qty': <10}{'Price': <10}{'Value': <10}")
for stock, qty in user_portifolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{'Stock': <10}{'Qty': <10}{'Price': <10}{'Value': <10}")
print(f"\n total Investment value: ${total_value}")

#savimg to CSV file
save = input("\nDo you want to save this summary to a CSV file?  (yes/no): ").lower()
if save == "yes":
    with open("stock-tracker.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["stock", "Quantity", "Price", "Total value"])
        for stock, qty in user_portifolio.items():
            price = stock_prices[stock]
            value = price * qty
            writer.writerow([stock, qty, price, value])


        writer.writerow([])
        writer.writerow(["Total", "", "", total_value])
        print("✅ Summary saved to 'portfolio_summary.csv'.")

































