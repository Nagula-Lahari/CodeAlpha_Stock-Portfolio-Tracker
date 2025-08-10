# CodeAlpha - Task 2: Stock Portfolio Tracker

# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 120,
    "MSFT": 300,
    "AMZN": 140
}

# Function to calculate total investment
def calculate_investment():
    portfolio = {}  # store user stocks
    total_value = 0

    print("=== Stock Portfolio Tracker ===")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    while True:
        stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if stock_name == "DONE":
            break
        if stock_name not in stock_prices:
            print("❌ Stock not found! Please choose from available list.")
            continue

        try:
            qty = int(input(f"Enter quantity of {stock_name}: "))
            if qty <= 0:
                print("❌ Quantity must be positive!")
                continue
        except ValueError:
            print("❌ Please enter a valid number for quantity!")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + qty
        print(f"✅ Added {qty} shares of {stock_name}")

    # Calculate total investment
    print("\n=== Portfolio Summary ===")
    for stock, qty in portfolio.items():
        stock_value = stock_prices[stock] * qty
        print(f"{stock} - {qty} shares - Value: ${stock_value}")
        total_value += stock_value

    print(f"\n💰 Total Investment Value: ${total_value}")

    # Save to file
    save_choice = input("\nDo you want to save this summary to a file? (y/n): ").lower()
    if save_choice == "y":
        file_name = "portfolio_summary.txt"
        with open(file_name, "w") as f:
            f.write("=== Portfolio Summary ===\n")
            for stock, qty in portfolio.items():
                stock_value = stock_prices[stock] * qty
                f.write(f"{stock} - {qty} shares - Value: ${stock_value}\n")
            f.write(f"\nTotal Investment Value: ${total_value}\n")
        print(f"📄 Summary saved to {file_name}")

if __name__ == "__main__":
    calculate_investment()
