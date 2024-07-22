from django.urls import path
from .views import BooksListView

#book_urls
urlpatterns = [
  path('', BooksListView.as_view(), name='book_list')
]
