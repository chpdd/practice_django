from django.apps import AppConfig
from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('user_edit/', views.UserEditView.as_view(), name='user_edit'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('sign_in/', views.SignInView.as_view(), name='sign_in'),
    path('log_out/', views.CustomLogOutView.as_view(), name='log_out'),
]
