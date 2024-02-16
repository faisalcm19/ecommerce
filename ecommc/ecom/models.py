from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    Category_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

    def __str__(self) :
        return self.Category_name
    
class product(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image',null=True)
    description=models.CharField(max_length=300)

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    options=(
        ('in-cart','in-cart'),
        ('cancelled','cancelled'),
        ('order','order')
)
    status=models.CharField(max_length=300,choices=options,default='in-cart')


class Oders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    carts=models.ForeignKey(Carts,on_delete=models.CASCADE)
    order_date=models.DateField(auto_now_add=True)
    address=models.TextField(max_length=255)
    email=models.EmailField(null=True)
    
    options=(
        ('order-placed','order-placed'),
        ('cancelled','canecelled'),
        ('dispatched','dispatched'),
        ('deliverd','deliverd'),
    )
    status=models.CharField(max_length=300,choices=options,default='order-placed')     

    
