from .models import Boards
from rest_framework import serializers


class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = '__all__'
        # soll alle Felder anzeigen