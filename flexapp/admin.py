from distutils.log import Log
from django.contrib import admin
from .models import Cart, Customer, Login, Product, Signup

# Register your models here.

admin.site.register(Login)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Signup)