from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from categories.models import Category

from .models import Transaction
from .permissions import IsAuthorUser
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
        Transaction.objects.create(owner_id=request.data['owner'], sum=request.data['sum'], category=category,
                                   description=request.data.get('description', ''))
        sum_to_add = prev_sum + int(request.data['sum'])
        category.spent_sum = sum_to_add
        request.user.current_balance -= int(request.data['sum'])
        if request.user.current_balance >= 0:
            category.save()
            request.user.save()
            serializer = TransactionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)
        else:
            return Response({"Current user don't have enough balance for this actions"})

    def get_permissions(self):
        if self.action in ['update', 'destroy',
                           'retrieve']:
            permission_classes = [IsAuthorUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
