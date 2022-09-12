# from asyncio.locks import _ContextManagerMixin
from multiprocessing import context
from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def index(requeset):
    return HttpResponse("Welcome")


def product_details(request):
    return render(request, "shop-details.html")



def shop_page(request):
    products = Product_sub_category_details.objects.all()
    context = {
        'products' : products
    }
    return render(request, "shop-grid.html", context)



def search(request):
    query = request.GET['search']
    subproducts = Product_sub_category_details.objects.filter(product_mst__name__icontains=query)
    context = {
        'subproducts' : subproducts
    }
    return render(request, "shop-details.html", context)
