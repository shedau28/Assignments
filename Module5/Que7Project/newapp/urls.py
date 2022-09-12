from django.urls import path
from .views import *

urlpatterns = [
    path("", shop_page, name='shop-grid'),
    path("shop_page/", shop_page, name='shop_page'),
    path("product_details/", product_details, name='product_details'),
    path("search/", search, name='search'),
]