from rest_framework import serializers
from bookingapp.models import Hotel, Room, Client, Reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'address']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['hotel', 'room_number', 'room_type', 'price_per_night']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['hotel', 'room', 'client', 'check_in_date', 'check_out_date']


