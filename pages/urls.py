from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('telehealth/', views.telehealth, name='telehealth'),
    path('merch/', views.merch, name='merch'),
    path('about/', views.about, name='about'),
]
