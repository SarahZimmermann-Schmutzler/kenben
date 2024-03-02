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
    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ('creator',)


class SubtasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'
        

class TicketsSerializer(serializers.ModelSerializer):
    subtasks = SubtasksSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        assigned_to = validated_data.pop('assigned_to', None)
        if assigned_to is not None:
            # generates an instance of the field --> replaced with new value
            instance.assigned_to.set(assigned_to)

        # other fields are processed
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
    
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description', 'creator', 'created_at', 'checked', 'assigned_to', 'priority', 'status', 'due_date', 'board', 'time_till_due', 'subtasks', 'assigned_to_usernames']
        read_only_fields = ('creator',)

