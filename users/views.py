from django.shortcuts import render, redirect
from .forms import RegisterationForm
from django.contrib.auth import authenticate, login

def register(request):

    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password= password)
            login(request,user)
            return redirect('blog-home')

    else:
        form = RegisterationForm()

    context = {'form':form}
    return render(request, 'users/register.html',context)
