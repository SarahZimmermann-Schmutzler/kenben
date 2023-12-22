from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Boards, Tickets
from .serializers import BoardsSerializer, TicketsSerializer

# Create your views here.

class BoardsView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Returns a list of all Boards.
        """
        # boards = Boards.objects.filter(creator=request.user)
        boards = Boards.objects.all()
        # sollen nur die Boards des Users angezeigt werden
        serializer = BoardsSerializer(boards, many=True)
        return Response(serializer.data)

class TicketsView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Returns a list of all Tickets.
        """
        # boards = Boards.objects.filter(creator=request.user)
        tickets = Tickets.objects.all()
        # sollen nur die Boards des Users angezeigt werden
        serializer = TicketsSerializer(tickets, many=True)
        return Response(serializer.data)