from rest_framework import serializers
from tickets.models import Guest, Movies, Reservation

class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'


class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class GuestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

