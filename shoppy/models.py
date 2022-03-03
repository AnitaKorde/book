from itertools import product
from unicodedata import category, name
from django.db import models

# Create your models here.
class Common(models.Model):
   
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True


class Product(Common):
   
    category=models.CharField(max_length=200)
    
    class Meta:
        db_table="product"



class Prod_category(Common):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table="prod_category"


class Prod_color(Common):
    
    color_code=models.CharField(max_length=100)
    product=models.ManyToManyField(Product)

    class Meta:
        db_table="prod_color"


class Apparel_size(Common):

    code=models.CharField(max_length=100)
    sort_order=models.CharField(max_length=100)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table="prod_size"