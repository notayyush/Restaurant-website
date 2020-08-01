from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

# Create your views here.

# def about(request):
#     return HttpResponse("This is about page")
# def services(request):
#     return HttpResponse("This is Services page")
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        Email=request.POST.get('Email')
        Phone=request.POST.get('Phone')
        desc=request.POST.get('desc')
        date=datetime.today()
        contactobj=Contact(name=name,Email=Email,Phone=Phone,desc=desc,date=datetime.today())
        contactobj.save()
        messages.success(request, 'your message has been sent!')
    return render(request,'contacts.html')
def index(request):
    
    # if request.user.is_anonymous:
    #     return redirect("/login")
    return render(request,'index.html')
# def loginUser(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request,user)
#             return redirect("/")
    
#         else:
#             return render(request,'login.html')
#     return render(request,'login.html')
    
# def logoutUser(request):
#     logout(request)
#     return redirect("/login")
# def signup(request):
#     if request.method == "POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
        
#     return render(request,'signup.html')
    