from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from flexapp import views
from django.conf import settings
from django.conf.urls.static import static
# from flexapp.forms import LoginForm
from .forms import LoginForm

urlpatterns = [
    path('',views.home, name="home"),
    path('detail',views.detail, name="detail"),
    path('feed',views.feed, name="feed"),
    path('product',views.product, name="product"),
    path('product1',views.product1, name="product1"),
    # path('registration', auth_views.LoginView.as_view(template_name='registration.html', authentication_form=LoginForm)),
    path('registration',views.registration, name="registration"),
    # path('signup',views.SignupView.as_view(),name="signup"),
    path('signup',views.signup, name="signup"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)