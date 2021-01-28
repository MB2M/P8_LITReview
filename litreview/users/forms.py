from django import forms

from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_repeat']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    # username = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(widget=forms.EmailInput(
    #     attrs={'class': 'form-control'}))
    # password = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password_repeat = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phone_number = forms.CharField(widget=forms.NumberInput(
    #     attrs={'class': 'form-control'}), required=False)
