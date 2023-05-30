from rest_framework import serializers
from .models import (
    BookInstance,
    Book,
    Genre,
    Author,
)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'summary', 'isbn', 'genre')


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ('id', 'book', 'imprint', 'due_back', 'LOAN_STATUS')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'firstname', 'lastname', 'date_of_birth', 'date_of_death')
