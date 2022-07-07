from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Author, Book
from rest_framework.response import Response
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import status



# Create your views here.
@api_view(['GET'])
def authors_list(request):
    try:
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_one_author(request, id):
    try:
        author = Author.objects.get(id=id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def new_author(request):
    try:
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as err:
        print(err)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def edit_author(request, id):
    try:
        author = Author.objects.get(id=id)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as err:
        print(err)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_author(request, id):
    try:
        author = Author.objects.get(id=id)
        if author:
            author.delete()
        return Response({}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def new_book(request):
    try:
        author_id = request.data['author']
        author = Author.objects.get(id=author_id)
        book = Book(
            title=request.data['title'],
            description=request.data['description'],
            author=author
        )
        book.save()
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        print('error: ', err)
        return Response({}, status=status.HTTP_502_BAD_GATEWAY)

@api_view(['GET'])
def book_list(request):
    try:
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_one_book(request,id):
    try:
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Exception as err:
        print(err)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
        if book:
            book.delete()
            return Response({}, status=status.HTTP_202_ACCEPTED)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        print(err)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def edit_book(request, id):
    try:
        book = Book.objects.get(id=id)
        author = Author.objects.get(id=request.data['author'])
        if book and author:
            book.title = request.data['title']
            book.description = request.data['description']
            book.author = author
            book.save()
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        print(err)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def many_books(request):
    try:
        for element in request.data:
            print(element)
            author = Author.objects.get(id=element['author'])
            book = Book(
                title=element['title'],
                description=element['description'],
                author=author
            )
            book.save()
        return Response({"status": "created"}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
