from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Ticket
from .forms import TicketForm

@login_required
def feed(request):
    tickets = Ticket.objects.filter(user=request.user.id)
    return render(request, 'reviews/feed.html', locals())

@login_required
def add_ticket(request, ticket_id=None):
    ticket = Ticket.objects.get(pk=ticket_id) if ticket_id is not None else None
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('reviews:feed')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'reviews/addticket.html', {'form': form})

@login_required
def view_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'reviews/viewticket.html', locals())

@login_required
def update_ticket(request):
    pass

@login_required
def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.delete()
    return redirect('reviews:feed')
