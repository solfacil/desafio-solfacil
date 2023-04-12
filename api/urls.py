from django.urls import include, path
from rest_framework import routers

from api.views import ParceiroViewSet

router = routers.DefaultRouter()
router.register(r'parceiro', ParceiroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
