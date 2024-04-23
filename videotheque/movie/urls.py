from django.urls import path
from movie import views as movie_views

urlpatterns = [
    path('directors/', movie_views.director_list_view, name='director_list'),
    path('directors/<int:id>', movie_views.director_detail_view, name='director_defails'),
]
