from plotly.offline import plot
import plotly.graph_objs as go 
import pandas as pd
from datetime import datetime
import requests

def get_data():
    url = 'https://api.unibit.ai/v2/stock/historical?tickers=AAPL,WORK&interval=1&startDate=2019-09-15&endDate=2019-09-20&selectedFields=all&accessKey=Demo'
    res = requests.get(url)
    res = res.json()['result_data']['AAPL']
    return res
def get_simple_candlestick():
    data = get_data()
    x,y,z,w,k = [],[],[],[],[]

    for item in data:
        x.append(item['date'])
        y.append(item['open'])
        z.append(item['high'])
        w.append(item['low'])
        k.append(item['close'])
    tracel = go.Candlestick(
        x = x,
        open = y,
        high = z,
        low = w,
        close = k
    )
    layout = go.Layout(
        xaxis = dict(autorange=True),
        yaxis = dict(autorange=True)
    )
    plot_data = [tracel]
    figure = go.Figure(data = plot_data, layout = layout)
    plot_div = plot(figure, output_type = 'div', include_plotlyjs = False)
    return plot_div
print(get_simple_candlestick())