from django .urls import path
from . views import reverse


urlpatterns = [
    path("reverse/",reverse.as_view()),
]

