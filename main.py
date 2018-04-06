import CIK
import plotting
import utils
import argparse

# Branch based on command line arguments
skipIntro = None
parser = argparse.ArgumentParser()
parser.add_argument("-q", "--query", type=str, help="Supply a query from command line to run this script without user input")
args = parser.parse_args()
if args.query:
    argList = args.query.split(',')
    if argList.__len__() == 2:
        symbol = argList[0].strip()
        metric = argList[1].strip()
        skipIntro = True


# Ask user for stock symbol and metric
if not skipIntro:
    utils.print_welcome()
    symbol, metric = utils.get_inputs()

# Translate symbol into CIK
symbolCIK = CIK.get_ciks([symbol])

# Get data for that CIK
data = CIK.get_data_by_cik(symbolCIK[symbol])

# Plot what the user wanted
plotting.line(data, "Date", metric, symbol)