from django.urls import path
from . import views
urlpatterns = [path('', views.index_add_ex1, name='index'),]