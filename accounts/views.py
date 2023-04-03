from accounts import my_forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = my_forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account has been created, please login.")
            return redirect('user-login')
    else:
        form = my_forms.UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required()
def mybar(request):
    return render(request, 'accounts/mybar.html')