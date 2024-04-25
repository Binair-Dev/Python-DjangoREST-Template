from django.urls import path
from django.urls.conf import include
from .views import DirectorViewset, MovieViewset
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'directors', DirectorViewset)
# router.register(r'movies', MovieViewset)

director_list = DirectorViewset.as_view({
    'get': 'list',
    'post': 'create'
})

director_detail = DirectorViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

movie_list = MovieViewset.as_view({
    'get': 'list',
    'post': 'create'
})

movie_detail = MovieViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

movie_custom_delete = MovieViewset.as_view({
    'delete': 'custom_delete'
})

urlpatterns = [
    #path('', include(router.urls))
    path('directors/', director_list, name='director-list'),
    path('directors/<int:pk>/', director_detail, name='director-detail'),

    path('movies/', movie_list, name='movie-list'),
    path('movies/<int:pk>/', movie_detail, name='movie-detail'),
    path('movies/<int:pk>/delete/', movie_custom_delete, name='movie-custom-delete'),
]
