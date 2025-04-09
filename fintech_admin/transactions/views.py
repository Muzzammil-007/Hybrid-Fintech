from django.shortcuts import render

# Create your views here.
# transactions/views.py
from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = ['status', 'user']  # Enable filtering by status, user
    ordering_fields = ['amount', 'timestamp']