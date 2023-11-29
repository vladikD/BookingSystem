from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Hotel, Room, Reservation
from .serializers import HotelSerializer, RoomSerializer, ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class HotelListView(APIView):
    def get(self, request, format=None):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hotel = self.get_object(pk)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        hotel = self.get_object(pk)
        serializer = HotelSerializer(hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hotel = self.get_object(pk)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RoomListView(APIView):
    def get(self, request, format=None):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReservationListView(APIView):

    # authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservationDetailView(APIView):

    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

# ..........Оновлення данних в резервації
    def patch(self, request, reservation_id, format=None):
        reservation = self.get_object(reservation_id)
        if reservation is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ReservationSerializer(reservation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  ............Видалення резервації
    def delete(self, request, pk, format=None):
        reservation = self.get_object(pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)