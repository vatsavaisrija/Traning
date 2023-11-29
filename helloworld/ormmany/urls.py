from django .urls import path
from .views import *

urlpatterns = [
    path("funone/",funone.as_view()),
    path("funtwo/",funtwo.as_view()),
    path("funthree/",funthree.as_view()),
    path("GetModel/",GetModel.as_view()),
]

