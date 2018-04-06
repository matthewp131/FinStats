import re, requests
import csv
import os
import utils


# The getCIKs function is adapted from https://gist.github.com/dougvk/8499335
def get_ciks(TICKERS):
    URL = 'http://www.sec.gov/cgi-bin/browse-edgar?CIK={}&Find=Search&owner=exclude&action=getcompany'
    CIK_RE = re.compile(r'.*CIK=(\d{10}).*')
    cik_dict = {}
    for ticker in TICKERS:
        f = requests.get(URL.format(ticker), stream = True)
        results = CIK_RE.findall(f.text)
        if len(results):
            results[0] = int(re.sub('\.[0]*', '.', results[0]))
            cik_dict[str(ticker).upper()] = str(results[0])
    return cik_dict


def get_data_by_cik(cik):
    readfile = open(os.path.join("data","companies","".join([cik,"-quarterly.csv"])), mode="r")
    reader = csv.reader(readfile)
    dict = {rows[0]: rows[1:] for rows in reader}
    readfile.close()

    dataset = {key: dict[value] for key, value in utils.short_names.items()}

    return dataset

