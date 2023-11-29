from django.urls import path,include
from .import views


urlpatterns = [
    path('restauth/',views.RegisterAPI.as_view()),
    path('login/',views.LoginAPI.as_view()),
]