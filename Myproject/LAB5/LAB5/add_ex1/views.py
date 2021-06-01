# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def index_add_ex1(request):
     return render(request, 'add_ex.html')