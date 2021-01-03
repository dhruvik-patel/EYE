from django.shortcuts import render, redirect
from .models import *

def about(request):
    return render(request,'about.html')

def home(request):
    images = Image.objects.all()
    cats = Category.objects.all()
    return render(request,'home.html', {'images':images,'cats':cats})

def category_images(request, cid):
    cats = Category.objects.all()
    cat = Category.objects.get(pk=cid)
    images = Image.objects.filter(cat=cat)
    myid = cid
    return render(request,'home.html', {'images':images,'cats':cats, 'myid':myid})

def main(request):
    cats = Category.objects.all()
    return render(request,'main.html', {'cats':cats})
