from django.shortcuts import render
from .forms import registerForm
# Create your views here.
def registerPage(request):
    form = registerForm()
    return render(request,'loginPage.html',{"form":form})