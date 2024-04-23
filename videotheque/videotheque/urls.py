from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index_view, name='index'),

    path('movies/', include('movie.urls')),
]
