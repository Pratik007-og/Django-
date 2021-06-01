from django.urls import path
from . import views
urlpatterns = [ path('home', views.index_add_ex2, name='index'),
                path('metadata',views.meta,name='metadata'),
                path('review',views.review,name='review'),
                path('publisher',views.publisher,name='publisher'),
                ]