from django.urls import path
from.views import *


urlpatterns = [
    path("post/",Register.as_view()),
    path("login/",Login.as_view())
]