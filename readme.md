# FinStats
A simple program to plot Earnings per Share or Gross Profit for NYSE symbols.
Uses plotly offline to generate plot and show in user's default browser.

### Setup
Download archive.zip at http://usfundamentals.com/archive.zip, rename it data, and put it inside the repo, such that the repo looks like:
<pre><code> FinStats/
         ...
	 data/
	 ...
	 main.py</code></pre>

### Running
usage: <code>main.py [-h] [-q QUERY]</code>

optional arguments:
* <code>-h, --help</code> show this help message and exit
* <code>-q QUERY, --query QUERY</code> Supply a query from command line to run this script without user input
