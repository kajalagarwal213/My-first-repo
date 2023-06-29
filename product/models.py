from django.db import models

# Create your models here.
class Apparel_size(models.Model):
    size_id=models.IntegerField()
    size_code=models.CharField(max_length=120)
    sort_order=models.CharField(max_length=120)
    
class Product(models.Model):
    Apparel_sizes=models.ForeignKey(Apparel_size,on_delete=models.CASCADE) 
    product_name=models.CharField(max_length=120)
    product_id=models.IntegerField()
    other_data=models.CharField(max_length=120)
    
class Product_Categories(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE) 
    category_id=models.IntegerField()
    
class Categories(models.Model):
    product_Categories=models.ForeignKey(Product_Categories,on_delete=models.CASCADE)
    category_id=models.IntegerField()
    parent_category_id=models.IntegerField()
    category_name=models.CharField(max_length=120)
    
    
class Product_colour(models.Model):
    product=models.ManyToManyField(Product)
    color_id=models.IntegerField()
    
class Color(models.Model):
    Productcolour=models.ForeignKey(Product_colour,on_delete=models.CASCADE)
    colorid=models.IntegerField()
    color_code=models.CharField(max_length=120)
    color_name=models.CharField(max_length=120)