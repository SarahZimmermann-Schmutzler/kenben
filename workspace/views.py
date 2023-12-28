from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Board, Ticket, Subtask
from .serializers import BoardsSerializer, TicketsSerializer, SubtasksSerializer

# Create your views here.
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class BoardsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Returns a list of all Boards.
        """
        # boards = Boards.objects.filter(creator=request.user)
        boards = Board.objects.all()
        # sollen nur die Boards des Users angezeigt werden
        serializer = BoardsSerializer(boards, many=True)
        return Response(serializer.data)


class TicketsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Returns a list of all Tickets.
        """
        # boards = Boards.objects.filter(creator=request.user)
        tickets = Ticket.objects.all()
        # sollen nur die Boards des Users angezeigt werden
        serializer = TicketsSerializer(tickets, many=True)
        return Response(serializer.data)


class SubtasksView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Returns a list of all Subtasks.
        """
        # boards = Boards.objects.filter(creator=request.user)
        subtasks = Subtask.objects.all()
        # sollen nur die Boards des Users angezeigt werden
        serializer = SubtasksSerializer(subtasks, many=True)
        return Response(serializer.data)