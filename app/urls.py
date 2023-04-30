from django.urls import path
from app import views
from .views import  list_partners, upload_csv , list_address_partners

urlpatterns = [
    path('', views.app, name='home'),
    path('partners/', list_partners, name='partners-list'),
    path('partners/address/', list_address_partners, name='partners-address-list'),
    path('uploadCsv/', upload_csv, name='upload_csv'),
]
