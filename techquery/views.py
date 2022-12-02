from django.shortcuts import render , HttpResponse , redirect
from django.contrib import messages , auth
from django.contrib.auth.models import User
from django.contrib.auth import logout



# Create your views here.



def index(request):
    return render(request,'index.html')
    

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')

def info(request):
    return render(request, 'info.html')

def contact(request):
    return render(request,'contact.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password =request.POST['password']
        confirm_password= request.POST['confirm_password']


        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username exists')
                return redirect('login')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already exists')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    messages.success(request,"Your account has been sucessfully created")
                    return redirect('login')
        else:
            messages.error(request,'Password do not match')
            return redirect('signup')
    
    return render(request,'signup.html')

   