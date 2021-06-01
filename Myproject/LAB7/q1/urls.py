from django.urls import path
from . import views
urlpatterns = [path('',views.home_page,name = 'home_page'),
               path('category',views.category,name = 'category'),
               path('page',views.page,name = 'page'),
               path('display',views.display,name = 'display'),]