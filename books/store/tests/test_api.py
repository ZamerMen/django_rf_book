from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='test book1', price=25)
        book_2 = Book.objects.create(name='test book2', price=35)
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        serializer_data = BooksSerializer([book_1, book_2], many=True).data
        self.assertEqual(response.data, serializer_data)

