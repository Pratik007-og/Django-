from django.urls import path
from . import views
urlpatterns = [path('',views.home_page,name = 'home_page'),
               path('works',views.works_page,name = 'works'),
               path('lives',views.lives_page,name = 'lives'),
               path('display',views.display,name = 'display'),
               ]