from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

# from authors.views import AuthorViewSet,BookViewSet,BiographyViewSet
# from library.view_exam import BookViewSet
# from libraty.view_example import BookListAPIView


# from libraty.view_example import get
# from libraty.view_example import BookViewSet
# BookLimitOffsetPaginatonViewSet
# from libraty.view_example import get
# from libraty.view_example import BookCustomViewSet
# from libraty.view_example import  BookListAPIView
from library.view_e import  BookLimitOffsetPaginatonViewSet
# from libraty.view_example import BookAPIView
# from library.view_exam import BookModelViewSet

# from library.view_exam import BookDjangoFilterViewSet
# from library.view_exam import BookAPIView
# from library.view_exam import get
# from library.view_exam import BookCustomViewSet
from library.view_e import BookAPIView, get, BookViewSet, BookModelViewSet, BookCustomViewSet, \
    BookQuerysetFilterViewSet, BookFilterListAPIView, BookFilterModelViewSet, BookDjangoFilterViewSet

router = DefaultRouter()
# from libraty.view_example import BookModelViewSet
# from libraty.view_example import BookModelViewSet
router.register('book_model_view', BookDjangoFilterViewSet)

# router = SimpleRouter()
# router.register('book_f', BookDjangoFilterViewSet)
router.register('book_p', BookLimitOffsetPaginatonViewSet)
# router.register('biography', BiographyViewSet)


from library.view_e import BookCreateAPIView,BookRetrieveAPIView,BookDestroyAPIView,BookListAPIView,BookUpdateAPIView


# level 3
# router.register('book', BookViewSet,basename='book')
#
# # level 4
# router.register('book_model', BookModelViewSet)
#
# # level 5
# router.register('book_custom', BookCustomViewSet)
#
# #Filter
# router.register('book_filter', BookQuerysetFilterViewSet)


#
# router.register('book', BookViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/', include(router.urls)),

    # level 1
    # path('api/book', BookAPIView.as_view()),
    # path('api/book_get', get),
    #
    # # level 2
    # path('api/list/', BookListAPIView.as_view()),
    # path('api/create/', BookCreateAPIView.as_view()),
    # path('api/update/<int:pk>/', BookUpdateAPIView.as_view()),
    # path('api/delete/<int:pk>/', BookDestroyAPIView.as_view()),
    # path('api/detail/<int:pk>/', BookRetrieveAPIView.as_view()),


    # # level 3 - 5
    path('api/', include(router.urls)),

    # filter part_2
    path('api/<str:name>/', BookFilterListAPIView.as_view()),
    #
    # path('api/', include(router.urls)),


]
# Footer