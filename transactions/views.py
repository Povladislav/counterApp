from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from categories.models import Category

from .models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    lookup_field = "id"

    def create(self, request, *args, **kwargs):
        category_pk = request.data['category']
        category = Category.objects.get(pk=category_pk)
        prev_sum = category.spent_sum
        Transaction.objects.create(sum=request.data['sum'], category=category,
                                   description=request.data.get('description', ''))
        sum_to_add = prev_sum + int(request.data['sum'])
        category.spent_sum = sum_to_add
        category.save()
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
