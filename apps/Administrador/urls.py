from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('new_concentration_area/', new_concentration_area),
    path('new_keyword/', new_keyword),
    path('keyword_list/', keyword_list),
    path('concentration_area_list/', concentration_area_list)
]
