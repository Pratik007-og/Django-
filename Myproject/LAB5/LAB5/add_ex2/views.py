# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def index_add_ex2(request):
     return render(request, 'add_ex2.html')
def meta(request):
    return render(request, 'metadata.html')
def review(request):
    return render(request, 'reviews.html')
def publisher(request):
    return render(request, 'publisher.html')
