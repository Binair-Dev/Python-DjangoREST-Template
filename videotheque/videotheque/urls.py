from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),

    path('', views.index_view, name='index'),

    path('api/movies/', include('movie.urls')),
]
