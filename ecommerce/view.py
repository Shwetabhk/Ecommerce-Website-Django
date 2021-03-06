from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model
from .forms import ContactForm,LoginForm,RegisterForm
def home_page(request):
    context={
        "title":"Hello World!",
        "content":"Welcome to the home page!"
    }
    if request.user.is_authenticated():
        context["premium_content"]="Yeeeaaaahhhhhhh"
    return render(request,"homepage.html",context)
def contact_page(request):
    contact_form= ContactForm(request.POST or None)
    context={
        "title":"Contact!",
        "content":"You wanna contact me haan?",
        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,"contact/view.html",context)
def about_page():
    context={
        "title":"About!",
        "content":"Know all about me bro!"
    }
    return render(request,"homepage.html",context)
def login_page(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    print("User logged in")
    #print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)
        #print(request.user.is_authenticated())
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            print("Error")
    return render(request,"auth/login.html",context)
User=get_user_model()
def register_page(request):
    form=RegisterForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        email=form.cleaned_data.get("email")
        new_user=User.objects.create_user(username,email,password)
        print(new_user) 
        if new_user is not None:
            return redirect("/login")
    return render(request,"auth/register.html",context)