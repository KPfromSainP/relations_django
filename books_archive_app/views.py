from .models import (
    Book,
    BookInstance,
    Genre,
    Author,
)
from .serializers import (
    BookSerializer,
    BookInstanceSerializer,
    GenreSerializer,
    AuthorSerializer
)
from rest_framework import generics
from django.template import loader
from django.http import HttpResponse


def index(request):
    # entries = Members.objects.all()
    # entries.delete()
    template = loader.get_template('hrefs.html')
    return HttpResponse(template.render())


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookInstanceListCreate(generics.ListCreateAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer


class GenreListCreate(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
