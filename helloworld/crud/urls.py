from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('verfication',views.verfication),
    path('update/<int:id>/',views.update),
    path('del/<int:id>/',views.delete),
    path('read/',views.read),

]