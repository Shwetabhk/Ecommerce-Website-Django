from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context={
        "title":"Hello World!",
        "content":"Welcome to the home page!"
    }
    return render(request,"homepage.html",context)
def contact(request):
    context={
        "title":"Contact!",
        "content":"You wanna contact me haan?"
    }
    if request.method=="POST":
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('yourcontent'))
    return render(request,"contact/view.html",context)
def about_page(request):
    context={
        "title":"About!",
        "content":"Know all about me bro!"
    }
    return render(request,"homepage.html",context)