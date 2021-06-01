from django.shortcuts import render
from .form import RegForm
# Create your views here.
def home_view(request):
    context = {}
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            manufacturer = form.cleaned_data['Manufacturer']
            model = form.cleaned_data['Model']
            context['manufacturer'] = manufacturer
            context['model'] = model
            return render(request,"result.html",context)
    else:
        form = RegForm()
        context['form'] = form
    return render(request,'base.html',context)
