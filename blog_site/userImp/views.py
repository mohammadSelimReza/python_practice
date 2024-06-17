from django.shortcuts import render,redirect
from .forms import registerForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully')
            form.save()
    else:
        form = registerForm()
    
    return render(request,'registration.html',{"form":form})

def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            userName = form.cleaned_data['username']
            userPassword = form.cleaned_data['password']
            user = authenticate(username=userName,password=userPassword)
            if user is not None:
                login(request,user)
                return redirect('blogPage')
    else:
        form = AuthenticationForm()
        return render(request,'loginPage.html',{'form':form})
    
def userLogout(request):
    logout(request)
    return('homePage')
                
    