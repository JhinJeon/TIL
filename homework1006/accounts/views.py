from django.shortcuts import render, redirect
from django.contrib.auth import login, logout as auth_login, auth_logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def signup(request):
    if request.user.is_authenticated():
        return redirect('either:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')

    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


def login(request):
    return


def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
    return redirect('either:index')