from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Portfolio,Product,Agent,Service

# Create your views here.
def about(request):
    agents=Agent.objects.all()
    services=Service.objects.all()
    products = Product.objects.order_by('?')[:3]
    context={
        "agents":agents,
        "services":services,
        "products":products
    }
    return render(request,"about_us.html",context)

def checkout(request):
    return render (request,"checkout.html")

def google_map(request):
    return render(request,"google_map_location.html")

def our_portfolio(request):
    portfolio_list = Portfolio.objects.all()
    paginator = Paginator(portfolio_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "page_obj": page_obj
    }
    return render(request, "our_portfolio.html", context)

def portfolio_details(requset):
    return render(requset,"portfolio_details.html")

def product_details(request):
    return render(request,"product_details.html")

def shop(request):
    products=Product.objects.all()
    paginator=Paginator(products,8)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    context={
        "page_obj":page_obj
    }
    return render(request,"shop.html",context)

