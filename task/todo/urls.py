from django.urls import path
from .views import *

urlpatterns= [
    path('post/',userregistrationview.as_view()),
    path('create/',userRegisterAPI.as_view()),
    path('put/<int:id>/',updatebyid.as_view()),
    path('get/<int:id>/', getbyid.as_view()),
    path('get_all/',getall.as_view()),
]