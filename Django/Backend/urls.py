from django .urls import path
from .views import *

urlpatterns = [
    path('singup/',singup.as_view()),
    path('singin/',login.as_view()),
    path('update/<int:id>/',update.as_view()),
    path('forgot/<int:id>/',forgot.as_view()),
    path('getall/',getall.as_view()),
    path('getbyid/<int:id>/',getbyid.as_view()),
    path('post/',details.as_view()),
    path('detailsupdate/<int:id>/',detailsupdate.as_view()),
    path('getalldetails/',getalldetails.as_view()),
    path('getbyskills/<str:skills>/',getbyskills.as_view()),
    path('getbystream/<str:stream>/',getbystream.as_view()),
    path('getbyyear/<int:year>/',getbyyear.as_view()),
    path('getbyscore/<path:score>/',getbyscore.as_view()),
    path('getbyemail/<str:email>/',getbyemail.as_view()),
    path('getdetailsbyid/<int:user_details>/',getdetailsbyid.as_view())
]