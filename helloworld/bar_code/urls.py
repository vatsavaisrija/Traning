from django .urls import path
from .views import *


urlpatterns = [
    path('post/',create.as_view()),
]