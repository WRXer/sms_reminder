from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import MainConfig
from .views import RecipientViewSet



app_name = MainConfig.name

router = DefaultRouter()
router.register(r'recipient', RecipientViewSet, basename='recipients')


urlpatterns = [
    path('', include(router.urls)),
]