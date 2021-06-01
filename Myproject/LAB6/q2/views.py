from django.shortcuts import render
from .forms import my_form
# Create your views here.
def home_view():
    context = {}
    if request.method == "POST":
        form = my_form(request.POST)
        if form.is_valid():
            name = form['name']
            roll_no = form['roll_no']
            subject = form['subject']
            context['name'] = name
            context['roll'] = roll_no
            context['subject'] = subject
            return render(request,"page2.html",context)
    else:
        form = my_form()
        context['form'] = form
        return render(request,"page1.html",context)