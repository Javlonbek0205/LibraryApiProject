from rest_framework.generics import ListAPIView
from books.models import Book
from .serializers import BookSerializer

# Create your views here.
class  BookAPIView(ListAPIView):  #json formatga olib o`tilishi uchun yozildi
  queryset = Book.objects.all()
  serializer_class = BookSerializer