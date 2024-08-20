from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404, redirect
from .models import Portfolio,Product,Agent,Service,Comment
from django.contrib import messages
from .forms import ContactForm,CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request,"homepage.html")

def agent(request):
    return render(request,"agent.html")

# @login_required(login_url="login")
def agent_details(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Thank you for your message.')
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = ContactForm()
    return render(request, 'agent__details.html', {'form': form})

def news(request):
    return render(request,"news.html")

def news_details(request):
    return render(request, "news__details.html")

def wishlist(request):
    return render(request,"wishlist.html")

def my_cart(request):
    return render(request, "my__cart.html")

def services(request):
    return render(request,"services.html")

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

def portfolio_details(request, id):
    portfolio_details = get_object_or_404(Portfolio, id=id)
    portfolios = Portfolio.objects.order_by('?')[:3]

    context = {
        "portfolio_details": portfolio_details,
        "portfolios": portfolios
    }

    return render(request, "portfolio_details.html", context)

def product_details(request, id):
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
    
    promo_product = Product.objects.order_by('?')[:2]
    product = get_object_or_404(Product, id=id)
    portfolios = Portfolio.objects.order_by('?')[:3]
    comments=Comment.objects.all()
    
    
    context = {
        "product": product,
        "promo_product": promo_product,
        'portfolios': portfolios,
        'comments':comments
    }
    return render(request, "product_details.html", context)

def shop(request):
    keyword = request.GET.get("keyword")
    products = Product.objects.all()

    if keyword:
        products = products.filter(product_name__icontains=keyword)

    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "keyword": keyword
    }

    return render(request, "shop.html", context)


# Contact Form


