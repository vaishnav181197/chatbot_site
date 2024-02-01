from django.urls import path
from .views import *


urlpatterns=[
    path('sin',SignInView.as_view(),name="sin"),
    path('sup',SignUpView.as_view(),name="sup")
    
]