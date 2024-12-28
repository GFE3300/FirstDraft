from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

class NoteListCreate(generics.ListCreateAPIView): # ListCreateAPIView is a generic view that provides GET (list) and POST method handlers
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user # Get the authenticated user
        return Note.objects.filter(author=user) # Return only notes created by the authenticated user

    def perform_create(self, serializer):
        if serializer.is_valid(): 
            serializer.save(author=self.request.user) 
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView): # CreateAPIView is a generic view that provides POST method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]