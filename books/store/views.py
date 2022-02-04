from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
