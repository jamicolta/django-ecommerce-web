from django.urls import path
from .views import register

app_name = 'user'

urlpatterns = [
    path('accounts/register', register, name='register')
]