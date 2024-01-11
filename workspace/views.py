from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .models import Board, Ticket, Subtask
from .serializers import BoardsSerializer, TicketsSerializer, SubtasksSerializer, UserSerializer

# Create your views here.
class RegisterView(APIView):
    """
    API view for User-Registration.
    validates and creates new user account, if user (email-adress) does not already exists
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if User.objects.filter(email=request.data["email"]).exists():
            return Response({"error": "Email already exists"})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user": serializer.data})



class LoginView(ObtainAuthToken):
    """
    API View for User-Login. 
    provides token-based authentication: login, validating, returning auth-token with userdetails
    """
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

    def get(self, request, boardId=None, format=None):
        """
        Returns a list of all Boards.
        """
        if boardId:
            board = Board.objects.get(id=boardId)
            serializer = BoardsSerializer(board, many=False)
            return Response(serializer.data)
        else:
            boards = Board.objects.filter(creator=request.user)
            # boards = Board.objects.all()
            # sollen nur die Boards des Users angezeigt werden
            serializer = BoardsSerializer(boards, many=True)
            return Response(serializer.data)
        

        # boards = Board.objects.filter(creator=request.user)
        #     # boards = Board.objects.all()
        #     # sollen nur die Boards des Users angezeigt werden
        # serializer = BoardsSerializer(boards, many=True)
        # return Response(serializer.data)
    
    
    def post(self, request, format=None):
        """
        Saves a new created board in the backend.
        """
        serializer = BoardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data)
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