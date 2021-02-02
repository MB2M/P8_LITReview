from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.utils import IntegrityError

from .models import Review, Ticket, UserFollows
from .forms import FollowForm, TicketForm, ReviewForm



@login_required
def feed(request):
    tickets = Ticket.objects.filter(user=request.user.id)
    return render(request, 'reviews/feed.html', locals())


@login_required
def add_ticket(request, ticket_id=None):
    ticket = get_object_or_404(
        Ticket, pk=ticket_id, user=request.user.id) if ticket_id is not None else None
    if request.method == 'POST':
        form_ticket = TicketForm(request.POST, instance=ticket)
        if form_ticket.is_valid():
            ticket = form_ticket.save(commit=False)
            if ticket.user_id is None:
                ticket.user = request.user
            ticket.save()
            return redirect('reviews:feed')
    else:
        form_ticket = TicketForm(instance=ticket)
    return render(request, 'reviews/addticket.html', {
        'form_ticket': form_ticket,
    })

# @login_required
# def add_ticket_2(request, ticket_id=None, review=False):
#     ticket = get_object_or_404(Ticket, pk=ticket_id) if ticket_id is not None else None
#     if request.method == 'POST':
#         form_ticket = TicketForm(request.POST, instance=ticket)
#         if form_ticket.is_valid():
#             ticket = form_ticket.save(commit=False)
#             if ticket.user_id is None:
#                 ticket.user = request.user
#             if review:
#                 form_review = ReviewForm(request.POST)
#                 if form_review.is_valid():
#                     ticket.save()
#                     review = form_review.save(commit=False)
#                     review.user = request.user
#                     review.ticket = ticket
#                     review.save()
#             else:
#                 ticket.save()
#             return redirect('reviews:feed')

#     else:
#         form_ticket = TicketForm(instance=ticket)
#         form_review = ReviewForm()
#     return render(request, 'reviews/addticket.html', {
#         'form_ticket': form_ticket,
#         'form_review': form_review,
#         })


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'reviews/viewticket.html', locals())


@login_required
def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id, user=request.user.id)
    ticket.delete()
    return redirect('reviews:feed')


@login_required
def new_review(request):
    if request.method == 'POST':
        form_ticket = TicketForm(request.POST)
        form_review = ReviewForm(request.POST)
        if form_ticket.is_valid() and form_review.is_valid():
            ticket = form_ticket.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = form_review.save(commit=False)
            review.rating = request.POST['rating']
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('reviews:feed')
    else:
        form_ticket = TicketForm()
        form_review = ReviewForm()
    return render(request, 'reviews/newreview.html', {
        'form_ticket': form_ticket,
        'form_review': form_review,
        'max_rate': range(6),
    })


@login_required
def review_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    user_review = ticket.review_set.filter(user_id=request.user.id)
    if user_review:
        review = user_review[0]
        print('------', review.rating)
    else:
        review = None
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.rating = request.POST['rating']
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('reviews:feed')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/reviewticket.html', {
        'ticket': ticket,
        'form': form,
        'max_rate': range(6),
        'review': review,
    })


@login_required
def subscribes(request):
    error_message = ""
    user_id = request.user.id
    followers = UserFollows.objects.filter(user=user_id)
    follows = UserFollows.objects.filter(followed_user=user_id)
    if request.method == 'POST':
        form = FollowForm(request.POST)
        if form.is_valid():
            follow_username = form.cleaned_data['follow_username']
            follow_user = User.objects.filter(username=follow_username)
            if len(follow_user) > 0:
                follow = UserFollows()
                follow.user = follow_user[0]
                follow.followed_user = request.user
                if follow.user != follow.followed_user:
                    try:
                        follow.save()
                    except IntegrityError:
                        error_message = 'User already added'
                else:
                    error_message = 'you can\'t follow yourself'
            else:
                error_message = 'Unknow username'
    else:
        form = FollowForm()
    return render(request, 'reviews/subscribes.html', {
        'followers': followers,
        'follows': follows,
        'form': form,
        'error_message': error_message,
    })

@login_required
def unsubscribe(request, user_follow_id):
    user_follow = UserFollows.objects.get(pk=user_follow_id, user=request.user.id)
    user_follow.delete()
    return redirect('reviews:subscribes')