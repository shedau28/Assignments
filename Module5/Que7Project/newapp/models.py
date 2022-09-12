from ast import Pass
from email.policy import default
from django.db import models

# Create your models here.

class Product_mst(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, default="")

    def __str__(self) -> str:
        return self.name

class Product_sub_category_details(models.Model):
    product_mst = models.ForeignKey(Product_mst, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=30, default="")
    price = models.IntegerField()
    description = models.CharField(max_length=200, default="")
    porduct_image = models.ImageField(upload_to="media/product_images", default="media/default.png")

    def __str__(self) -> str:
        return self.model_name



# o There will be 2 modules(Admin,Product manager)

# o Admin can add product name (ex.Product id and product name) 
# ex. (1, Samsung), (2, Apple)...etc. Data should store in 
# Product_mst table with product id as primary key

# o Admin can add product subcategory details Like (Product price, 
# product image,

# o Product model, product Ram) data should store in 
# Product_sub_cat table

# o Admin can get product name as foreign key from product_mst 
# table in product_sub_category_details page

# o Admin can view, update and delete all registered details of 
# product

# o product manager can search product on search bar and get all 
# details about product
    
