from django.http import HttpResponse
from django.shortcuts import render,redirect

def home_page(request):
    context={"content":"Welcome to home page"}

    return render(request,'home_page.html',context)
