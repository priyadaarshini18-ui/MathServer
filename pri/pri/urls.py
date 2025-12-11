from django.urls import path
from mathapp import views

urlpatterns = [
    path('', views.rate, name='rate'),
]
