def print_welcome():
    print("Welcome to Stock Plotter!")
    print("Enter a query in the following format: [SYMBOL, METRIC]")
    print("\tSYMBOL: Any standard NYSE symbol")
    print("\tMETRIC: 'EPS' or 'GP'")
    print("\t\tEPS: Earnings per Share")
    print("\t\tGP: Gross Profit")


def get_inputs():
    args = input("Enter query: ")
    args = args.split(',')
    i = 0
    for arg in args:
        args[i] = arg.strip()
        i += 1
    symbol = args[0].upper()
    metric = args[1].upper()

    return symbol, metric


short_names = {
    "Date": "",
    "EPS": "EarningsPerShareBasic",
    "GP": "GrossProfit"
}

units = {
    "Date": "MM/DD/YYYY",
    "EPS": "USD/share",
    "GP": "USD"
}