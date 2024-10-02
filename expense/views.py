from django.shortcuts import render
from .models import Transaction
from rest_framework.response import Response
from .serializers import TransactionSerializer
from rest_framework.decorators import api_view

@api_view()
def get_Transaction(request):
    queryset = Transaction.objects.all()
    serializer = TransactionSerializer(queryset , many = True)
    
    return Response({
        "data" : serializer.data
    })
    