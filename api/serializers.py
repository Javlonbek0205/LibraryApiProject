from rest_framework import serializers #---> Book modelini json malumotga olib o`tish uchun chaqirildi`
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ('title', 'subtitle', 'author', 'isbn')