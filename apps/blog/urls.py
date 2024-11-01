from django.urls import path
from .views import blogView

app_name = 'blog'

urlpatterns = [
    path('', blogView, name='blog'),
]