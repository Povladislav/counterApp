from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from transactions.permissions import IsAuthorUser

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    lookup_field = "id"

    def create(self, request, *args, **kwargs):
        Category.objects.create(owner_id=request.data['owner'],
                                name_of_category=request.data['name_of_category'],
                                spent_sum=request.data.get('spent_sum', 0))

        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['update', 'destroy',
                           'retrieve']:
            permission_classes = [IsAuthorUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
