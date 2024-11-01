from django.urls import path
from .views import transactionsView

app_name = 'honey'

urlpatterns = [
    path('', transactionsView, name='transactions'),
]