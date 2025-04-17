from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):
    class ReviewDetailSerializers(serializers.ModelSerializer):
        class Meta:
            model=Review
            fields = ('content', 'score',)


    review_set=ReviewDetailSerializers( many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class BookisbnSerializer(serializers.ModelSerializer):
        class Meta:
            model=Book
            fields=('isbn',)
    
    book=BookisbnSerializer()

    class Meta:
        model=Review
        fields = ('book','content', 'score',)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)