from django.urls import path
from .import views

urlpatterns= [
    path('company/',views.CompanyAPI.as_view()),
    path('employee/',views.employeeAPI.as_view()),
    path('otom/', views.employee1API.as_view()),
]