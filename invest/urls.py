from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('mining_farms', views.mining_farms, name='mining_farms'),
    path('investment', views.investment, name='investment'),
    path('mining_farms/<int:farm_id>', views.invest, name='investment'),
]
