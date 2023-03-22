from django.shortcuts import render
import yfinance as yf
import matplotlib.pyplot as plt

 #  isme saare keys h
# Create your views here.

def home(request):


    sensex = yf.Ticker('^BSESN')
    # print(sensex.fast_info)
    sensex = sensex.fast_info['last_price']
    # print(sensex.fast_info)
    sensex = round(sensex,2)

    nifty= yf.Ticker('^NSEI')
    niftybank= yf.Ticker('^NSEBANK')
    niftyIT = yf.Ticker('^CNXIT')
    infi = yf.Ticker('INFY.NS')
    reliance = yf.Ticker('RELIANCE.NS')
    hdfc = yf.Ticker('HDFCBANK.NS')
    asianpaint = yf.Ticker('ASIANPAINT.NS')
    niftymid = yf.Ticker('NIFTY_MIDCAP_100.NS')
    nifty150 = yf.Ticker('NIFTY_MIDCAP_150.NS')
    # return HttpResponse("Hello, world. I didn't want to wake up. I was having a much better time asleep.")
    nifty=round(nifty.fast_info['last_price'],2)
    niftybank=round(niftybank.fast_info['last_price'],2)
    niftyIT=round(niftyIT.fast_info['last_price'],2)
    infi=round(infi.fast_info['last_price'],2)
    reliance = round(reliance.fast_info['last_price'],2)
    hdfc = round(hdfc.fast_info['last_price'],2)
    asianpaint = round(asianpaint.fast_info['last_price'],2)
    niftymid = round(niftymid.fast_info['last_price'],2)
    nifty150 = round(nifty150.fast_info['last_price'],2)
    context = {'sensex': sensex,'nifty150':nifty150,'niftymid':niftymid,'nifty': nifty, 'niftybank': niftybank, "niftyIT": niftyIT , "infi":infi ,'reliance':reliance,'hdfc':hdfc,'asianpaint':asianpaint }


    return render(request,'index1.html',context)

def stocklist(request):
    return render(request,'allstocklist.html')

def stockdetail(request):
    return render(request,'stockdetail.html')

def portfolio(request):
    return render(request,'portfolio.html')