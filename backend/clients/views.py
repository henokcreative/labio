from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from .models import Message, Contract
from .serializers import MessageSerializer, ContractSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer