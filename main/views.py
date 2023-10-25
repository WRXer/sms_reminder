from rest_framework import viewsets

from .models import Recipient
from .serializers import RecipientSerializer


class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer

    def perform_create(self, serializer):
        """
        Сохраняем продукт в базе данных с автором, который является текущим пользователем, отправившим запрос.
        """
        serializer.save(author=self.request.user)