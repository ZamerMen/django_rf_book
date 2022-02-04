from rest_framework.serializers import ModelSerializer

from .models import *


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'