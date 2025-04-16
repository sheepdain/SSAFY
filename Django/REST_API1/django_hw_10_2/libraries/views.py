from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import LibrariesListSerialzer, LibrariesSerialzer


# Create your views here.
@api_view(['GET'])
def libraries_list(request):
    books=Book.objects.all()
    serializer=LibrariesListSerialzer(books, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def libraries_detail(request, book_pk):
    book=Book.objects.get(pk=book_pk)
    serializer=LibrariesSerialzer(book)
    return Response(serializer.data)