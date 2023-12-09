from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views
from .views import register_user


urlpatterns = [
    path('hotels/', views.HotelListView.as_view()),
    path('hotels/<int:pk>/', views.HotelDetailView.as_view()),
    path('rooms/', views.RoomListView.as_view()),
    path('reservations/', views.ReservationListView.as_view()),
    path('reservations/<int:pk>/', views.ReservationDetailView.as_view(), name='reservation-detail'),
    path('auth/', include('djoser.urls')), #djoser  використовуємо для створення користувача
    path('register/', register_user, name='register_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #drf jwt/ d в гуглі передаєм назву і пароль
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #drf jwt / також в гуглі
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

