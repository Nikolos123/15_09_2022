from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.


from .serializers import AuthorModelSerializer
from .models import Author

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer