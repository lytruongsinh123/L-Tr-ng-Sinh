from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,  'page/Home.html')
def contact(request):
    return render(request, 'page/contact.html')
def error(request, exception):
    return render(request, 'page/error.html', {'message': exception})
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'page/register.html',{'form':form})