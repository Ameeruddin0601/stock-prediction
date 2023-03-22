from django.shortcuts import render

# Create your views here.

def home(request):
    # return HttpResponse("Hello, world. I didn't want to wake up. I was having a much better time asleep.")
    return render(request,'index1.html')

def stocklist(request):
    return render(request,'allstocklist.html')

def stockdetail(request):
    return render(request,'stockdetail.html')