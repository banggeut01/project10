from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.db.models import Q # 리드미
def index(request):
    # users = User.objects.filter(~Q(username='admin'))
    accounts = User.objects.all()
    context = {
        'accounts': accounts
    }
    return render(request, 'accounts/index.html', context)

def detail(request, account_pk):
    account = get_object_or_404(User, id=account_pk)
    context = {
        'account': account
    }
    return render(request, 'accounts/profile.html', context)

def signup(request):
    return render(request, 'accounts/form.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('movies:index')