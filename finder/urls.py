from django.urls import path
from . import views

app_name = 'finder'

urlpatterns = [
    path('', views.facility_search, name='search'),
]
