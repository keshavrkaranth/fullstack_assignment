from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import registrationForm

# Create your views here.


def index_page(request):
    return render(request, 'index.html')


def user_signup(request):
    form = registrationForm()
    if request.method == 'POST':
        form = registrationForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data['password'])
    return render(request, 'signup.html', {'form': form})
