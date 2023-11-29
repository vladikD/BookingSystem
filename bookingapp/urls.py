from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views


urlpatterns = [
    path('hotels/', views.HotelListView.as_view()),
    path('hotels/<int:pk>/', views.HotelDetailView.as_view()),
    path('rooms/', views.RoomListView.as_view()),
    path('reservations/', views.ReservationListView.as_view()),
    path('reservations/<int:pk>/', views.ReservationDetailView.as_view(), name='reservation-detail'),
    path('auth/', include('djoser.urls')), #djoser token
    #path('auth/', include('djoser.urls.authtoken')), #djoser token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #drf jwt
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #drf jwt
    path('/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

