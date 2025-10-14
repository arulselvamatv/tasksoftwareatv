from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, SignupForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:index')  
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})



from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('authentication:login')


def profile_settings(request):
    return render(request, 'authentication/profile_settings.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = SignupForm()
    return render(request, 'authentication/signup.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'authentication/password_reset.html'
    success_url = reverse_lazy('password_reset_done')



