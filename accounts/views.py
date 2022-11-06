from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm
#from .models import Person

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

def login_user():
    pass

def logout_user():
    pass