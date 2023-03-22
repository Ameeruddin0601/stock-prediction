from django.shortcuts import render, redirect
from django.http import HttpResponse

###
import yfinance as yf
import json
import yahoo_fin.stock_info as si
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create your views here.

def stock(request):
    if request.method == "POST":
        query = request.POST['query']
        if query:
            # Get the stock data
            t = query
            ticker = yf.Ticker(t)
            close_values = ticker.history(period="1y")["Close"].tolist()
            dates = ticker.history(period="1y").index.strftime("%Y-%m-%d").tolist()

            # Create a dictionary with the stock data
            data = {"close_value": close_values, "date": dates, "stock": query}
            print(data)

            # # Convert the dictionary to a JSON string
            # json_data = json.dumps(data)
            # json_data = json.dumps(t)

            # # Write the JSON string to a file
            # with open("data.json", "w") as file:
            #     file.write(json_data)
            return render(request, 'stockdetail.html', data)
    return render(request,'stockdetail.html')
    
# def search(request):
#     if request.method == "POST":

#         # def scraping(request):
#         ticker = request.POST.get('stock').upper() # name
#         STOCK = ticker
#         RANGE = ('2021-01-01','2021-12-31')    
#         price = si.get_live_price(STOCK)
#         hist_data_close = si.get_data(STOCK).loc[RANGE[0]:RANGE[1],['close']]
#         hist_data_adj = si.get_data(STOCK).loc[RANGE[0]:RANGE[1],['adjclose']]
#         # print(hist_data_close.head())
            
#         hist_data_close.plot(title=STOCK)
#         plt.savefig('stock/static/images/outputs/graph1.png')
#         # hist_data_adj.plot(title=STOCK)
#         # plt.savefig('stock/static/images/outputs/graph2.png')

#         hist_data_adj = hist_data_adj.rename(columns={'adjclose':STOCK})
#         norma = hist_data_adj / hist_data_adj.iloc[0,:]
#         norma["Rolling_Mean"] = norma[STOCK].rolling(window=20).mean()
#         norma.plot(title="Rolling_Mean")
#         plt.savefig('stock/static/images/outputs/graph2.png')

#         std = norma[STOCK].std()
#         norma['upper'] = norma['Rolling_Mean'] + 0.4*std
#         norma['lower'] = norma['Rolling_Mean'] - 0.4*std
#         norma.loc[:,[STOCK,'upper','lower']].plot(title='Bollinger Band')
#         plt.savefig('stock/static/images/outputs/graph3.png')

#         max_52 = int(hist_data_close.max())
#         min_52 = int(hist_data_close.min())

#         # _thread.start_new_thread(testsets, ())

#         context = {'name': ticker,'price': round(price, 3), 'max_52': max_52, "min_52": min_52}

#         return render(request,'search.html', context)
#         return HttpResponse(request.POST.get('query'))

def analysis(request):
    if request.method == 'POST':
        # ... process form data ...
        return render(request,'display.html')

    else:
        return render(request, 'display.html')
def analysis1(request):
    if request.method == "GET":
        query = request.GET['query']
        if query:
            # Get the stock data
            t = query
        ticker = t
        STOCK = ticker
        RANGE = ('2021-01-01','2021-12-31')    
        price = si.get_live_price(STOCK)
        hist_data_close = si.get_data(STOCK).loc[RANGE[0]:RANGE[1],['close']]
        hist_data_adj = si.get_data(STOCK).loc[RANGE[0]:RANGE[1],['adjclose']]
        # print(hist_data_close.head())
            
        hist_data_close.plot(title=STOCK)
        plt.savefig('sp/static/images/outputs/graph1.png')
        # hist_data_adj.plot(title=STOCK)
        # plt.savefig('stock/static/images/outputs/graph2.png')

        hist_data_adj = hist_data_adj.rename(columns={'adjclose':STOCK})
        norma = hist_data_adj / hist_data_adj.iloc[0,:]
        norma["Rolling_Mean"] = norma[STOCK].rolling(window=20).mean()
        norma.plot(title="Rolling_Mean")
        plt.savefig('sp/static/images/outputs/graph2.png')

        std = norma[STOCK].std()
        norma['upper'] = norma['Rolling_Mean'] + 0.4*std
        norma['lower'] = norma['Rolling_Mean'] - 0.4*std
        norma.loc[:,[STOCK,'upper','lower']].plot(title='Bollinger Band')
        plt.savefig('sp/static/images/outputs/graph3.png')

        max_52 = int(hist_data_close.max())
        min_52 = int(hist_data_close.min())

        # _thread.start_new_thread(testsets, ())

        context = {'name': ticker,'price': round(price, 3), 'max_52': max_52, "min_52": min_52}

        return render(request,'search.html', context)
        return HttpResponse(request.POST.get('query'))
