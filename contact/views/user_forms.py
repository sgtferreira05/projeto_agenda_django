from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from contact.forms import RegisterForm

def register(request):
    form = RegisterForm()

    messages.info(
        request,
        'Fill the form to register a new user.'
    )

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'User registered successfully.'
            )
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
            }
    )
def login_view(request):
        form = AuthenticationForm(request)

        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)

            if form.is_valid():
                user = form.get_user()
                auth.login(request, user)
                messages.success(
                    request,
                    'User logged in successfully.'
                )
                
                return redirect('contact:index')
            else:
                messages.error(
                    request,
                    'Invalid username or password.'
                )

        return render(
            request,
            'contact/login.html',
            {
                'form': form
            }
    )
def logout_view(request):
    auth.logout(request)
    messages.success(
        request,
        'User logged out successfully.'
    )
    return redirect('contact:login')