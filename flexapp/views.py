from .models import Login, Signup
from requests import Response
from django.views import View
from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def detail(request):
    return render(request, 'detail.html')

def product(request):
    return render(request, 'product.html')
def product1(request):
    return render(request, 'product1.html')

# def registration(request):
#     if request.method=="POST":
#         email=request.POST['email']
#         password=request.POST['password']
#         login=Login(email=email, password=password)
#         login.save()
#     return render(request, 'registration.html')
def registration(request):
    if request.method=="POST":
        signup = Signup.objects.filter(email=request.data["email"])
        if signup.password == request.data["password"]:
            return Response("Success")
        return Response("Incorrect password")
    return render(request, 'registration.html')

# class SignupView(View):
#     def get(self, request):
#         form = SignupForm()
#         return render (request, 'signup.html', {'form':form})
    
    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'signup.html',{'form':form})

def feed(request):
    return render(request, 'feed.html')

def signup(request):
    if request.method=="POST":
        name=request.POST['name']
        cname=request.POST['cname']
        email=request.POST['email']
        password=request.POST['password']
        signup=Signup(name=name,cname=cname,email=email, password=password)
        signup.save()
    return render(request, 'signup.html')
