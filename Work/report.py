import csv

def read_portfolio(filename):
    """Read a CSV file containing portfolio data and return a list of dictionaries."""
    portfolio = []
    with open(filename, 'r') as file:
        rows = csv.reader(file)
        headers = next(rows) # Skipping headers

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            if len(row) < 3:
                #print(f"Skipping malformed row: {rowno}")
                continue
            try:
                stock = {
                    'name'  : record['name'],
                    'shares': int(record['shares']),
                    'price' : float(record['price'])
                }
            except ValueError:
                print(f"Row: {rowno}. Bad row: {row}")
                continue
            portfolio.append(stock) # portfolio = list of dictionaries
    return portfolio

def read_prices(filename):
    """Read a CSV file containing current prices and return a dictionary."""
    prices = {} #dictionary
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 2:
                #print(f"Skipping malformed row: {row}")
                continue
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

def generate_report(portfolio, prices):
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']] #using the name of the stock in the portfolio.csv to look it up in the prices.csv file
        change        = current_price - stock['price']
        summary       = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def portfolio_report(portfoliofile,pricefile):        
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files 
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = generate_report(portfolio,prices)

    # Print it out
    print_report(report)

def print_report(report):
    # Output the report
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

portfolio_report('Data/portfolio.csv',
                 'Data/prices.csv')