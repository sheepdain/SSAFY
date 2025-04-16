from rest_framework import serializers
from .models import Book

class LibrariesListSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)

class LibrariesSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'