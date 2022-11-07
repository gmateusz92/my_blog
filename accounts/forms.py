from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'password1']

class AuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']

