from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required






def login(request):
    # I will suppose that the request method is POST, just like we did in the exercises. 
    name = request.POST.get('username')
    passw = request.POST.get('password')
    user = User.objects.get(username=name)
 
    if user.check_password(passw):
        return HttpResponse("Login successful")
    else:
        FailedLogins.objects.create(user=user, tried_passw=passw)    
        return HttpResponse("Invalid username or password")




@login_required
def your_information(request):
    name = request.POST.get('username')
    user = User.objects.get(username=name)

    if request.user.is_authenticated:
        response = []
        response.append(user.username)
        response.append(user.email)
        return HttpResponse(response)
    return redirect('/')

