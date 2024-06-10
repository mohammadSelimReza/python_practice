from django.shortcuts import render
from .forms import FormTesting

# Create your views here.
def formPage(request):
    form = FormTesting()
    return render(request, 'formPractice.html',{'form':form})