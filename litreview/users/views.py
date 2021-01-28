from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm

def user_register(request):
    template = 'users/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("username exist")
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                print("username exist")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect('/reviews/')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})