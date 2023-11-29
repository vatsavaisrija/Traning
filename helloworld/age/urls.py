from django .urls import path
from .views import *

urlpatterns = [
    path('get/',reverse.as_view())
]