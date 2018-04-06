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
> python main.py
> python main.py --query "MSFT,EPS"
