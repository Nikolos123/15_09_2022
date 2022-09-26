from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    get_object_or_404

# from authors.filters import BookFilter
# from authors.filters import BookFilter
from authors.filters import BookFilter
from authors.models import Book
from authors.serializers import BookModelSerializer

# level 1 APIView
class BookAPIView(APIView):
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    #http://127.0.0.1:8000/api/book
    def get(self,request,format=None):
        book = Book.objects.all()
        serializer = BookModelSerializer(book, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        pass
# #
@api_view(['GET']) ##'POST'
# @renderer_classes([JSONRenderer,BrowsableAPIRenderer])
def get(request):
      if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookModelSerializer(book, many=True)
        # return Response(serializer.data)
        return Response({'test':1})###Дополнительный пример
      elif request.method == 'POST':
          pass

# level 2 Generic views
class BookCreateAPIView(CreateAPIView):
   renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer

class BookListAPIView(ListAPIView):
   renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer
# #
class BookRetrieveAPIView(RetrieveAPIView):
   renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer
#
class BookDestroyAPIView(DestroyAPIView):
   renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer

class BookUpdateAPIView(UpdateAPIView):
   renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer

# level 3 ViewSets


class BookViewSet(ViewSet):
   renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
   # {"name": "test",
   #  "authors": [2, 3]}
   def post(self,request):
       book = BookModelSerializer(data=request.data)
       book.is_valid()
       book.save()
       return Response(book.data)


   def list(self,request):#список
       book = Book.objects.all()
       serializer_class = BookModelSerializer(book,many=True)
       return Response(serializer_class.data)

   def retrieve(self,request,pk=None):#детализация
       book = get_object_or_404(Book, pk=pk)
       serializer_class = BookModelSerializer(book)
       return Response(serializer_class.data)

   def destroy(self,request,pk=None):
       instance = get_object_or_404(Book, pk=pk)
       instance.delete()
       book = Book.objects.all()
       serializer_class = BookModelSerializer(book, many=True)
       return Response(serializer_class.data)
#     #
   @action(detail=True, methods=['get'])
   def only(self, request, pk=None):
       book = Book.objects.get(id=pk)
       return Response({'book': book.name,'id':book.id})



# level 4 ModelViewSet (то что мы делали изначально самый просто способ)
class BookModelViewSet(ModelViewSet):
   # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer


# level 5 Custom ViewSet
#
# ListModelMixin,CreateAPIView, DestroyModelMixin,RetrieveAPIView,UpdateAPIView,GenericViewSet:
class BookCustomViewSet(ListModelMixin,DestroyModelMixin,GenericViewSet):
    queryset =  Book.objects.all()
    serializer_class =  BookModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


# filter
class BookQuerysetFilterViewSet(ModelViewSet):
   serializer_class = BookModelSerializer
   renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
   queryset = Book.objects.all()

   def get_queryset(self):
       return Book.objects.filter(name__contains='te1')#содержит
# #
#
class BookFilterListAPIView(ListAPIView):
   serializer_class = BookModelSerializer

   def get_queryset(self):
       name = self.kwargs['name']
       return Book.objects.filter(name__contains=name)

class BookFilterModelViewSet(ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer

   def get_queryset(self):
       name = self.request.query_params.get('name', '')
       book = Book.objects.all()
       if name:
           book = book.filter(name__contains=name)
       return book


#DjangoFilter
# filters.py ПОКАЗАТЬ НЕ ЗАБЫТЬ
class BookDjangoFilterViewSet(ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer
   # filterset_fields = ['id','name']
   filterset_class = BookFilter


# # #PAGINATOR
class BookLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 2
# # # # # #
# # # # # #
class BookLimitOffsetPaginatonViewSet(ModelViewSet):
   # renderer_classes = [JSONRenderer]
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer
   pagination_class = BookLimitOffsetPagination
       # BookLimitOffsetPagination