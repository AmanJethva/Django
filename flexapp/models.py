# from flexapp.forms import SignupForm
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Login(models.Model):
    email= models.CharField(max_length=100, default=0)
    password=models.CharField(max_length=50, default=0)

    def __str__(self):
        return self.email

class Signup(models.Model):
    name=models.CharField(max_length=100, default=0)
    cname=models.CharField(max_length=100, default=0)
    email=models.CharField(max_length=100, default=0)
    password=models.CharField(max_length=100, default=0)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()

    def __str__(self):
        return str(self.id)

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.TextField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images', default="")

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)