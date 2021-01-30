from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import RegisterForm

def user_register(request):
    template = 'users/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                user = form.save()
                # user = User.objects.create_user(
                #     form.cleaned_data['username'],
                #     form.cleaned_data['email'],
                #     form.cleaned_data['password']
                # )
                # user.save()

                login(request, user)

                return redirect('reviews:feed')

    else:
        form = RegisterForm()

    return render(request, template, {'form': form})