from django.shortcuts import render
from django.http import HttpResponse
from first.models import Name
from first.models import Name2


# Create your views here.
def fun(request):
    return HttpResponse("Hello from your first django application")
def home(request):
    if request.method=="POST":
        name=request.POST.get('name')
        home=Name(name=name)
        home.save()
    return render(request,"home.html")
def home2(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        home2=Name2(name=name,phone=phone,email=email)
        home2.save()
    return render(request,"home2.html")


    