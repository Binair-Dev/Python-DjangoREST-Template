from django.urls import path
from .views import DirectorList, MovieList, DirectorDetail, MovieDetail

urlpatterns = [
    path('directors/', DirectorList.as_view(), name='director_list'),
    path('directors/<int:id>', DirectorDetail.as_view(), name='director_details'),

    path('movies/', MovieList.as_view(), name='movie_list'),
    path('movies/<int:id>', MovieDetail.as_view(), name='movie_details'),
]
