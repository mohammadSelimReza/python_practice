from django.shortcuts import render, redirect
from .forms import MusicianForm
from . import models
from . import forms
def home(request):
    if request.method == 'POST':  # Check for POST method
        form = MusicianForm(request.POST)
        if form.is_valid():  # Correct method name
            form.save()
            return redirect('/')  # Use redirect after saving to avoid resubmission
    else:
        form = MusicianForm()
    
    return render(request, 'addmusician.html', {'form': form})

def edit_post(request, id):
    post = models.MusicianModel.objects.get(pk=id)
    form = forms.MusicianForm(instance=post)
    if request.method == 'POST':
        form =  forms.MusicianForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'addmusician.html', {'form': form})

def delete_post(request, id):
    post = models.MusicianModel.objects.get(pk=id) 
    post.delete()
    # return redirect('addTask')
    return redirect('/')