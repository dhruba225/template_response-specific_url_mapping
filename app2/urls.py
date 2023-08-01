app_name='nothing'
from django.urls import path
from app2.views import *

urlpatterns = [
    path('app2_first/',app2_first,name='app2_first'),
    path('app2_second/',app2_second,name='app2_second'),
]