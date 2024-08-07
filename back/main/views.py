from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,"about_us.html")

def checkout(request):
    return render (request,"checkout.html")

def google_map(request):
    return render(request,"google_map_location.html")

def our_portfolio(request):
    return render(request,"our_portfolio.html")

def portfolio_details(requset):
    return render(requset,"portfolio_details.html")

def product_details(request):
    return render(request,"product_details.html")

def shop(request):
    return render(request,"shop.html")