from django.urls import path
from . import views
urlpatterns = [path('', views.index4, name='index'),]