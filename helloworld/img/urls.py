from django .urls import path
from .views import *

urlpatterns = [
    path("post/",index),
    path("get/",table),
]