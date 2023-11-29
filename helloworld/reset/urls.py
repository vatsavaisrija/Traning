from django.urls import path
from .views import *

urlpatterns =[
    path('post/', registerAPI.as_view()),
    path('login/', loginAPI.as_view()),
    path('reset/<int:id>/', resetAPI.as_view()),

]