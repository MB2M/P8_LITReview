from django.shortcuts import render

from .models import Ticket

def feed(request):
    tickets = Ticket.objects.all()
    return render(request, 'reviews/feed.html', locals())