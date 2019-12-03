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
# def get_topographical_3D_surface_plot():
#     raw_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

#     data = [go.Surface(z=raw_data.as_matrix())]

#     layout = go.Layout(

#         autosize=False,
#         width=800,
#         height=700,
#         margin=dict(
#             l=65,
#             r=50,
#             b=65,
#             t=90
#             )
#         )
#     fig = go.Figure(data=data, layout=layout)
#     plot_div = plot(fig, output_type='div',filename='elevations-3d-surface')

#     return plot_div
# def pie_chart():
#     fig = {
#     "data": [
#         {
#         "values": [16, 15, 12, 6, 5, 4, 42],
#         "labels": [
#             "US",
#             "China",
#             "European Union",
#             "Russian Federation",
#             "Brazil",
#             "India",
#             "Rest of World"
#         ],
#         "domain": {"column": 0},
#         "name": "GHG Emissions",
#         "hoverinfo":"label+percent+name",
#         "hole": .4,
#         "type": "pie"
#         },
#         {
#         "values": [27, 11, 25, 8, 1, 3, 25],
#         "labels": [
#             "US",
#             "China",
#             "European Union",
#             "Russian Federation",
#             "Brazil",
#             "India",
#             "Rest of World"
#         ],
#         "text":["CO2"],
#         "textposition":"inside",
#         "domain": {"column": 1},
#         "name": "CO2 Emissions",
#         "hoverinfo":"label+percent+name",
#         "hole": .4,
#         "type": "pie"
#         }]
#     },
#     "layout": {
#         "title":"Global Emissions 1990-2011",
#         "grid": {"rows": 1, "columns": 2},
#         "annotations": [
#             {
#                 "font": {
#                     "size": 20
#                 },
#                 "showarrow": False,
#                 "text": "GHG",
#                 "x": 0.20,
#                 "y": 0.5
#             },
#             {
#                 "font": {
#                     "size": 20
#                 },
#                 "showarrow": False,
#                 "text": "CO2",
#                 "x": 0.8,
#                 "y": 0.5
#             }
#         ]
#     }

#     plot_div = plot(fig, output_type='div',filename='donut')
#     return plot_div