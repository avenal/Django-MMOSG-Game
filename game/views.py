from django.shortcuts import render, redirect
from accounts.models import CustomUser
from django.contrib import messages, auth
# Create your views here.
def login(request):
    if request.method == 'POST':
      # login user
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('login')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:    
        return render(request, 'game/login.html')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # check if password match
        if password == password2:
         # check username
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    user = CustomUser.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    messages.success(request, 'You are now registered')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:    
        return render(request, 'game/register.html')
    