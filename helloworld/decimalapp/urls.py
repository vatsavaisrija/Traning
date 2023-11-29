from django.urls import path
from .views import value

urlpatterns = [
    path('value/', value.as_view()),
]

