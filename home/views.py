from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *

def auth_user(request):
    register_form = UserRegistrationForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            register_form = UserRegistrationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()  
                login(request, user)  
                messages.success(request, 'Account created successfully!')
                return redirect('home') 

        elif 'login' in request.POST:
                if request.method == 'POST':
                    username = request.POST.get('userName')
                    password = request.POST.get('userPass')
                    user = authenticate(request, username=username, password=password)
                    
                    if user is not None:
                        if user.is_user():
                            login(request, user)
                            return redirect('home')
                        else:
                            messages.info(request, 'User does not have admin privileges.')
                    else: 
                        messages.info(request, 'UserName or password is incorrect!')

    return render(request, "apps/login_user.html", {'register_form': register_form})

def auth_admin(request):
    register_form_admin = AdminRegistrationForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            register_form_admin = AdminRegistrationForm(request.POST)
            if register_form_admin.is_valid():
                user = register_form_admin.save()  
                login(request, user)  
                messages.success(request, 'Account created successfully!')
                return redirect('home') 

        elif 'login' in request.POST:
            if request.method == 'POST':
                username = request.POST.get('adminName')
                password = request.POST.get('adminPass')
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    if user.is_admin():
                        login(request, user)
                        return redirect('home')
                    else:
                        messages.info(request, 'User does not have admin privileges.')
                else: 
                    messages.info(request, 'UserName or password is incorrect!')

    return render(request, "apps/login_admin.html", {'register_form_admin': register_form_admin})

def logoutPage(request):
    logout(request)
    return redirect('home')

@login_required
def add_tennis(request):
    if not request.user.is_admin():
        messages.error(request, 'Bạn không có quyền truy cập vào trang này.')
        return HttpResponseForbidden("Bạn không có quyền truy cập vào trang này.")

    if request.method == 'POST':
        form = TennisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sân tennis mới đã được thêm thành công!')
            return redirect('home')
    else:
        form = TennisForm()
    return render(request, 'apps/add_tennis.html', {'form': form})

def home(request):
    tennis = Tennis.objects.all()
    return render(request, "apps/index.html", {'tennis_courts': tennis})

def about(request):
    return render(request, "apps/about.html")

def property_list(request):
    tennis = Tennis.objects.all()
    return render(request, "apps/property-list.html", {'tennis_courts': tennis})

def property_type(request):
    return render(request, "apps/property-type.html")

def agent(request):
    return render(request, "apps/property-agent.html")

def testimonial(request):
    return render(request, "apps/testimonial.html")

def error(request):
    return render(request, "apps/404.html")

def contact(request):
    return render(request, "apps/contact.html")

def register(request):
    return render(request, "apps/register.html")

def login1(request):
    return render(request, "apps/login.html")



