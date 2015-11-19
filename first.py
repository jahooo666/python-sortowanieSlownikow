__author__ = 'Jasiek'

stock = {
    'GOOG': 520.53,
    'FB': 643.24,
    'YAHOO': 2.53,
    'AMZN': 100,
    'AAPL': 99.32
}

print min(zip(stock.values(), stock.keys()))
