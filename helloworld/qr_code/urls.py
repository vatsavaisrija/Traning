from django.urls import path
from .views import *

urlpatterns = [
    path('code/', home.as_view()),
    path('read/', upload),
]