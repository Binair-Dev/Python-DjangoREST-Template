from django.urls import path
from movie import views as movie_views

urlpatterns = [
    path('directors/', movie_views.director_list_view, name='director_list'),
    path('directors/<int:id>', movie_views.director_detail_view, name='director_details'),

    path('movies/', movie_views.movie_list_view, name='movie_list'),
    path('movies/<int:id>', movie_views.movie_details_view, name='movie_details'),
]
