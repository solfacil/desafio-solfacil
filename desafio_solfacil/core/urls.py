from rest_framework.routers import DefaultRouter

from django.urls import path, include
from desafio_solfacil.core import views

router = DefaultRouter()
router.register(r"parceiros", views.ParceiroView, basename="parceiros")

urlpatterns = [
    path("api/", include(router.urls)),
]
