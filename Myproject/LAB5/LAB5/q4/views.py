from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index4(request):
     return render(request, 'base4.html')