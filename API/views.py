from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# ListCreateAPIView handles GET and POST requests for listing and creating objects
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# RetrieveUpdateDestroyAPIView handles GET, PUT, PATCH, and DELETE requests for a single object
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
