from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


from .serializers import AuthorModelSerializer, BookModelSerializer, BiographiesHyperlinkedModelSerializer
from .models import Author, Book, Biographies


class AuthorModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BiographiesModelViewSet(ModelViewSet):
    queryset = Biographies.objects.all()
    serializer_class = BiographiesHyperlinkedModelSerializer
