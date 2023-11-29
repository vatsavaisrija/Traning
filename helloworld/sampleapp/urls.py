from django.urls import path
from.import views
urlpatterns = [

    path("house/",views.house),
    path("student/",views.student),
    path("members/",views.members)
]