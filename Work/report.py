import csv

def read_portfolio(filename):
    """Read a CSV file containing portfolio data and return a list of dictionaries."""
    portfolio = []
    with open(filename, 'r') as file:
        rows = csv.reader(file)
        headers = next(rows)  # Skip header row
        for rowno, row in enumerate(rows, start=1):
        	record = dict(zip(headers, row))
            if len(row) < 3:
                print(f"Skipping malformed row: {rowno}")
                continue
            try:
                holding = {
                    'symbol': row[0].strip(),
                    'shares': int(row[1].strip()),
                    'price': float(row[2].strip())
                }
            except ValueError:
                print(f"Row: {rowno}. Bad row: {row}")
                continue
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    """Read a CSV file containing current prices and return a dictionary."""
    prices = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 2:
                print(f"Skipping malformed row: {row}")
                continue
            try:
                symbol = row[0].strip()
                price = float(row[1].strip())
                prices[symbol] = price
            except ValueError as e:
                print(f"Couldn't parse row: {row}. Error: {e}")
                continue
    return prices

def compute_portfolio_value(portfolio, prices):
    """Compute the current value of the portfolio."""
    total_value = 0.0
    for holding in portfolio:
        symbol = holding['symbol']
        shares = holding['shares']
        purchase_price = holding['price']
        current_price = prices.get(symbol, 0.0)
        holding_value = shares * current_price
        total_value += holding_value
        gain_loss = (current_price - purchase_price) * shares
        print(f"{symbol}: Purchase Price = {purchase_price}, Current Price = {current_price}, Shares = {shares}, Gain/Loss = {gain_loss}")
    return total_value

# Example usage
portfolio = read_portfolio('C:\\Users\\Alan\\Desktop\\Python tut\\practical-python\\Work\\Data\\portfolio.csv')
prices = read_prices('C:\\Users\\Alan\\Desktop\\Python tut\\practical-python\\Work\\Data\\prices.csv')
total_value = compute_portfolio_value(portfolio, prices)
print(f"Total current value of the portfolio: {total_value}")
