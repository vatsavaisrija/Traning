from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("post/",create.as_view()),
    # path("update/<int:pk>",UpdateApi.as_view()),
    # path("read/",create.as_view()),
    # path("del/<int:id>",create.as_view()),
    path("getbyid/<int:id>/",getbyid.as_view()),
    path("update/<int:id>/",updatebyid.as_view()),
    path("delete/<int:id>/",deletebyid.as_view()),
]