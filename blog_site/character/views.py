from django.shortcuts import render,redirect
from .forms import CharacterForm
from django.contrib import messages
# Create your views here.
def character(request):
    form = CharacterForm()
    return render(request,'addCharacter.html',{'form':form})

def AddCharacter(request):
        if request.method == 'POST':
            form = CharacterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Character Added Successfully')
                form.save()
                return redirect('blogPage')
        else:
            form = CharacterForm()
            return render(request,'addCharacter.html',{'form':form})
       