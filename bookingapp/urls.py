from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('hotels/', views.HotelListView.as_view()),
    path('hotels/<int:pk>/', views.HotelDetailView.as_view()),
    path('rooms/', views.RoomListView.as_view()),
    path('reservations/', views.ReservationListView.as_view()),
    path('reservations/<int:pk>/', views.ReservationDetailView.as_view(), name='reservation-detail'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

