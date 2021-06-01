from django.shortcuts import render
from .forms import WorksForm,LivesForm
from .models import works,lives
# Create your views here.
def home_page(request):
    return render(request,"home_page.html")

def works_page(request):
    context = {}
    if request.method == "POST":
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = WorksForm()
        context['form'] = form
    return render(request,"works.html",context)

def lives_page(request):
    context = {}
    if request.method == "POST":
        form = LivesForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = LivesForm()
        context['form'] = form
    return render(request,"lives.html",context)

def display(request):
   work = works.objects.all()
   live = lives.objects.all()
   return render(request,'display.html',{"works":work,"lives":live})