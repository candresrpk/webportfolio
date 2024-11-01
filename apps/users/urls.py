from django.urls import path
from .views import loginView

app_name = 'users'

urlpatterns = [
    path('', loginView, name='login'),
]