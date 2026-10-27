stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0
portfolio = []

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input(
        "\nEnter stock name (or 'done' to finish): "
    ).upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        price = stock_prices[stock_name]
        investment = price * quantity

        total_investment += investment

        portfolio.append(
            (stock_name, quantity, price, investment)
        )

        print("Stock price: $", price)
        print("Investment value: $", investment)

    except ValueError:
        print("Please enter a valid whole number.")

print("\n----- Portfolio Summary -----")

for stock, quantity, price, investment in portfolio:
    print(
        stock,
        "| Quantity:", quantity,
        "| Price: $", price,
        "| Total: $", investment
    )

print("\nTotal investment value: $", total_investment)

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")

    for stock, quantity, price, investment in portfolio:
        file.write(
            f"{stock}, Quantity: {quantity}, "
            f"Price: ${price}, Investment: ${investment}\n"
        )

    file.write(
        f"\nTotal investment value: ${total_investment}\n"
    )

print("Portfolio saved to portfolio.txt")
