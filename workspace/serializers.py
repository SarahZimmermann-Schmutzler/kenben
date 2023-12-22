from .models import Boards, Tickets
from rest_framework import serializers


class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = '__all__'
        # soll alle Felder anzeigen

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'
        