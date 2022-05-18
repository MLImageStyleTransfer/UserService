from django.urls import path
from .views import *

urlpatterns = [
    path('user', user),
    path('sign-in', sign_in),
    path('sign-up', sign_up)
]