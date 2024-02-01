from django.urls import path
from .views import *


urlpatterns=[
    path('uhome',UserHomeView.as_view(),name='uhome'),
    path('cbot',ChatbotView.as_view(),name="cbot")
]