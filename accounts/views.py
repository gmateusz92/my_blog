from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm, AuthForm
#from .models import Person
from django.contrib import messages

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Zalogowanie użytkownika, a następnie przekierowanie go na stronę główną.
            authenticated_user = authenticate(username=username, password=raw_password)
            login(request, authenticated_user)
            return redirect('home')
    else:
        form = RegisterForm
    return render(request, 'accounts/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthForm
    return render(request, 'accounts/login.html', {'form': form, 'title': 'log in'})

def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')
