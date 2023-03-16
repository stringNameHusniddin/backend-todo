from django.shortcuts import render
from .models import ToDo
from .serializers import ToDoSerializers
from rest_framework import viewsets

# Create your views here.
class ToDoView(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers