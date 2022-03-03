from shoppy.models import Product
import random
import string

cat = {"TV":"Electronics","Fertinture":"Wooden"}
l=[]
for k in cat.keys():
    l.append(k)
#print(l)
a=random.choice(l)
b=cat.get(a)
#print(a)
#print(cat.get(a))