from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
def home_page(request):
    context={
        "title":"Hello World!",
        "content":"Welcome to the home page!"
    }
    return render(request,"homepage.html",context)
def contact(request):
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