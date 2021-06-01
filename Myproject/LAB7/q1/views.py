from django.shortcuts import render
from .forms import CategoryForm,PageForm
from .models import Category,Page
# Create your views here.
def home_page(request):
    return render(request,"home_page.html")

def category(request):
    context = {}
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/category')
            except:
                pass
    else:
        form = CategoryForm()
        context['form'] = form
    return render(request,'category.html',context)

def page(request):
   context1 = {}
   if request.method == "POST":
        form1 = PageForm(request.POST)
        if form1.is_valid():
            try:
                form1.save()
                return redirect('/page')
            except:
                pass
   else:
       form1 = PageForm()
       context1['form'] = form1
   return render(request,'page.html',context1)

def display(request):
   pages = Page.objects.all()
   categories = Category.objects.all()
   return render(request,'display.html',{"pages":pages,"categories":categories})
