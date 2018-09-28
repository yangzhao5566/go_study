"""
读写csv数据
"""

import csv
from collections import namedtuple

# with open('stocks.csv') as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     Row = namedtuple("Row", headers)
#     for r in f_csv:
#         row = Row(*r)
#         print(dict(row._asdict()))


with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(dict(row))

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]

with open("stock.csv", "w") as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

