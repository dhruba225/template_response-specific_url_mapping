app_name='something'
from django.urls import path
from app1.views import *

urlpatterns = [
    path('app1_first/',app1_first,name='app1_first'),
    path('app1_second/',app1_second,name='app1_second'),
]

