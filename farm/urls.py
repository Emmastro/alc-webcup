from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('edit_details', views.edit_details, name='edit_details'),
    path('investors', views.investors, name='investors'),
]
