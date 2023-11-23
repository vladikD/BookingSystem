from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views

urlpatterns = [
    path('hotels/', views.HotelListView.as_view()),
    path('rooms/', views.RoomListView.as_view()),
    path('clients/', views.ClientListView.as_view()),
    path('reservations/', views.ReservationListView.as_view()),


]

