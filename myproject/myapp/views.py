from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def payment_accounts(request):
    return render(request, 'myapp/payment_accounts.html')