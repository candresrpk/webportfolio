from django.shortcuts import render

# Create your views here.

def transactionsView(request):
    context = {
        'title': 'Transactions'
    }
    return render(request, 'honey/transactions.html', context)