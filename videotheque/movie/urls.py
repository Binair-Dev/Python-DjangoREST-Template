from django.urls import path
from .views import DirectorList, MovieList, DirectorDetail, MovieDetail

urlpatterns = [
    path('directors/', DirectorList.as_view(), name='director-list'),
    path('directors/<int:pk>', DirectorDetail.as_view(), name='director-detail'),

    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>', MovieDetail.as_view(), name='movie-detail'),
]
