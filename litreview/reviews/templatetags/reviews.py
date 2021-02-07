from reviews.models import Ticket, Review
from django import template

register = template.Library()



@register.filter
def ticket_review_of_user(value, user):

    return value.review_set.filter(user=user.id)

@register.filter
def lower(value):
    return value.lower()