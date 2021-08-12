from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
import re
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invaild credentails")
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if(first_name != "" or last_name != "" or username != "" or email != "" or password1 != "" or password2 != ""):
            if(password1==password2):
                if(re.match(regex, email)):
                    if User.objects.filter(username=username).exists():
                        # print(username)
                        messages.info(request, "Username Taken")
                        return redirect('register')   
                    elif User.objects.filter(email=email).exists():
                        messages.info(request, "Email Taken") 
                        return redirect('register')
                    
                    else:
                        user =  User.objects.create_user(username=username,password=password2, email=email, first_name=first_name, last_name=last_name)
                        user.save()
                        return redirect('login')
                else:
                    messages.info(request, "Enter valid Email Id") 
                    return redirect('register')
            else:
                messages.info(request, "Password Not matching")
                return redirect('register')
            return redirect('/')
        else:
            messages.info(request, "please fill all mandatory fields")
            return redirect('register')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')