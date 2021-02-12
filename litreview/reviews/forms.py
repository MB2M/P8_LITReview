from django import forms

from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'image': 'Image',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'body']
        labels = {
            'headline': 'Titre',
            'body': 'Commentaire'
        }
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class FollowForm(forms.Form):
    follow_username = forms.CharField(
        label='', max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
