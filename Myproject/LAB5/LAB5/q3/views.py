from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index3(request):
     return render(request, 'base3.html')