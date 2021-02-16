from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth.models import User


def user_register(request):
    template = 'users/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Les mots de passe ne correspondent pas'
                })
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password']
                )
                user.save()

                login(request, user)

                return redirect('reviews:feed')

    else:
        form = RegisterForm()

    return render(request, template, {'form': form})
