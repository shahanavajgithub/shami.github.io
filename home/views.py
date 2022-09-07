from unicodedata import name
from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.

def home(request):
    #return HttpResponse ("Hello Shami")
    return render(request, 'home.html')

def projects(request):
    #return HttpResponse ("Hello Shami !!! This is prjects page")
    return render(request, 'projects.html')
    

def about(request):
    #return HttpResponse ("Hello Shami !!! This is about page")
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']

        print(name,email,phone,desc)

        ins=Contact(name=name, email=email, phone=phone, desc=desc) 
        ins.save()
        print("Data Loaded into DB")

    #return HttpResponse ("Hello Shami !!! This is contact page")           
    return render(request, 'contact.html')