"""flexproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from flexapp import views

urlpatterns = [
    #user authentication
    # path('signup',views.sign_up),

    path('admin/', admin.site.urls),
    path('',include('flexapp.urls')),
    path('detail',include('flexapp.urls')),
    path('feed',include('flexapp.urls')),
    path('product',include('flexapp.urls')),
    path('registration',include('flexapp.urls')),
    path('signup',include('flexapp.urls')),
    path('sign_up',include('flexapp.urls')),
    path('product',include('flexapp.urls')),
    path('product1',include('flexapp.urls')),
    path('home1',include('flexapp.urls')),
]
