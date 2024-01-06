from .models import Board, Ticket, Subtask
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    creats and retrievs user instances
    """
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        
        return user
    
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {"password": {"write_only": True}}


class BoardsSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     board = Board.objects.create(
    #         creator=self.context['request'],
    #         title=validated_data['title'],
    #         )
    #     return board
    
    class Meta:
        model = Board
        fields = '__all__'
        # soll alle Felder anzeigen
        read_only_fields = ('creator',)

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class SubtasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'
        