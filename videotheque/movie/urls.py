from django.urls import path
from django.urls.conf import include
from .views import DirectorViewset, MovieViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'directors', DirectorViewset)
router.register(r'movies', MovieViewset)
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls))
]
