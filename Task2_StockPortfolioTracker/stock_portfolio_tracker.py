import csv
from datetime import datetime

# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

def main():
    portfolio = {}
    total_investment = 0

    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Enter stock name and quantity (type 'done' to finish)\n")

    while True:
        stock = input("Stock name: ").upper()
        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not found in price list. Try again.\n")
            continue

        try:
            qty = int(input("Quantity: "))
        except ValueError:
            print("Invalid quantity. Try again.\n")
            continue

        cost = stock_prices[stock] * qty
        portfolio[stock] = portfolio.get(stock, 0) + qty
        total_investment += cost
        print(f"Added {qty} shares of {stock} (${cost})\n")

    # Display summary
    print("\n----- Portfolio Summary -----")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        print(f"{stock}: {qty} shares x ${price} = ${qty * price}")
    print(f"Total Investment: ${total_investment}")

    if not portfolio:
        print("\nNo stocks added. Exiting without saving.")
        return

    # Save options
    save = input("\nSave result to file? (y/n): ").lower()
    if save == "y":
        file_format = input("Choose format - txt or csv: ").lower()

        if file_format == "csv":
            filename = "portfolio_summary.csv"
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Price per Share", "Total Cost"])
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    writer.writerow([stock, qty, price, qty * price])
                writer.writerow([])
                writer.writerow(["", "", "Total Investment", total_investment])
                writer.writerow(["", "", "Date", datetime.now().strftime("%Y-%m-%d %H:%M")])
            print(f"Saved to {filename}")

        else:
            filename = "portfolio_summary.txt"
            with open(filename, "w") as f:
                f.write("Portfolio Summary\n")
                f.write("------------------\n")
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    f.write(f"{stock}: {qty} shares x ${price} = ${qty * price}\n")
                f.write(f"Total Investment: ${total_investment}\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            print(f"Saved to {filename}")

if __name__ == "__main__":
    main()
