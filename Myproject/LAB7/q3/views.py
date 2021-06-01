from django.shortcuts import render
from .forms import AuthorForm,PublisherForm,BookForm
from .models import author,publisher,book
# Create your views here.
def home_page(request):
    return render(request,"home_page.html")

def author(request):
    context = {}
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/author')
            except:
                pass
    else:
        form = AuthorForm()
        context['form'] = form
    return render(request,'author.html',context)

def publisher(request):
   context1 = {}
   if request.method == "POST":
        form1 = PublisherForm(request.POST)
        if form1.is_valid():
            try:
                form1.save()
                return redirect('/publisher')
            except:
                pass
   else:
       form1 = PublisherForm()
       context1['form'] = form1
   return render(request,'publisher.html',context1)

def book(request):
   context1 = {}
   if request.method == "POST":
        form1 = BookForm(request.POST)
        if form1.is_valid():
            try:
                form1.save()
                return redirect('/book')
            except:
                pass
   else:
       form1 = BookForm()
       context1['form'] = form1
   return render(request,'book.html',context1)


def display(request):
   pages = Page.objects.all()
   categories = Category.objects.all()
   return render(request,'display.html',{"pages":pages,"categories":categories})
