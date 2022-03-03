from itertools import count
from operator import countOf
from unicodedata import name
from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from shoppy.db_shell import *
import random
#url: http://127.0.0.1:8001/


# Create your views here.
def Homepage(request):
    #print("in home page")
    #print(dir(request))
    #print(request.method)
    #return HttpResponse("<h1>Hi Hello</h1>")
    for i in range(0,10):
        a=random.choice(l)
        b=cat.get(a)
        Product.objects.create(name=a,category=b)
    all_prod=Product.objects.all()
    cont = {"Product":all_prod}
    return render(request,template_name="home.html",context=cont)

def show_data(request):
    all_prod=Product.objects.all()
    cont = {"Product":all_prod}
    return render(request,template_name="home.html",context=cont)

def drop_show(request):
    # s=set()
    # all_prod=Product.objects.all()
    # for i in all_prod:
    #     s.add(i.name)
    all= Product.objects.values_list("name",flat=True).distinct()
    all1= Product.objects.values_list("name").distinct()
    print(all)
    print(all1)
    cont = {"Product":all}
    return render(request,template_name="drop_lst.html",context=cont)
