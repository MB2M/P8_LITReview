from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.feed, name='feed'),
    path('addticket/', views.add_ticket, name='addticket'),
    path('addticket/<int:ticket_id>/', views.add_ticket, name='addticket'),
    path('<int:ticket_id>/', views.view_ticket, name='viewticket'),
    path('deleteticket/<int:ticket_id>/', views.delete_ticket, name='deleteticket'),
    path('newreview/', views.new_review, name='newreview'),
    path('<int:ticket_id>/review', views.review_ticket, name='reviewticket')
]