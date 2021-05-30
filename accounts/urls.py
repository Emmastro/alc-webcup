from django.urls import path
from . import views

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetDoneView, LogoutView, \
    PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

urlpatterns = [
    path('', views.account_redirect, name='accounts'),
    path('login/', views.signin, name='login'),
    path('register-farm/', views.register_farm, name='register-farm'),
    path('register-investor/', views.register_investor, name='register-investor'),
    path('logout/', LogoutView.as_view(
        template_name='registration/logout.html'), name='logout'),
]
