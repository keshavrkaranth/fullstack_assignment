from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import registrationForm, loginForm
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def index_page(request):
    return render(request, 'index.html')


def user_signup(request):
    form = registrationForm()
    if request.method == 'POST':
        form = registrationForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            usr = User.objects.create(first_name=cd['Name'],
                                      email=cd['Email'],
                                      username=cd['username'],
                                      password=cd['password'])
            usr.set_password(usr.password)
            usr.save()
            form = registrationForm()
            rest_usr = user.objects.create(
                user=usr, phone_no=cd['phone_number'])
            rest_usr.save()
            usr_login = authenticate(
                request, username=cd['username'], password=cd['password'])
            if usr_login is not None:
                if usr_login.is_active:
                    login(request, usr_login)
                    return redirect('restaurantapp:home')
    else:
        form = registrationForm()

    return render(request, 'signup.html', {'form': form})


def user_login(request):
    context = ''
    form = loginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usr = authenticate(request, username=username, password=password)
        if usr is not None:
            print('not none')
            if usr.is_active:
                print('active')
                login(request, usr)
                return redirect('restaurantapp:home')
            else:
                context = 'Disabled Acc'
        else:
            context = 'Invalid Credentials'

    else:

        form = loginForm()
    return render(request, 'login.html', {'form': form, 'msg': context})


def usr_logout(request):
    logout(request)
    return render(request, 'index.html')


@login_required
def log_home(request):
    rest_det = restaurant_details.objects.all()
    return render(request, 'home.html', {'details': rest_det})


def rest_details(request, pk):
    h = ''
    rst_detail = restaurant_details.objects.get(pk=pk)
    try:
        details = rest_dish_map.objects.get(restaurant=rst_detail.id)
        h = details.dishes.all()
    except:
        pass
    return render(request, 'details.html', {'dishes': h})
