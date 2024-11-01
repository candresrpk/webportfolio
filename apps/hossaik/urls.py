from django.urls import path
from .views import hossaikView

app_name = 'hossaik'

urlpatterns = [
    path('', hossaikView, name='index'),
]