from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
# Create your views here.
def addBlog(request):
        if request.method == 'POST':
            form = forms.BlogForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('blogPage')
        else:
            form = forms.BlogForm()
            
        return render(request,'addblog.html',{'form':form})
