from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('register/', views.register_user, name='register'),
    path('login/', views.logout_user, name='login_page'),
    path('logout/', views.login_user, name='logout_user'),

]