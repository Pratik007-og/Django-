from django.urls import path
from . import views
urlpatterns = [path('',views.home_page,name = 'home_page'),
               path('author',views.author,name = 'author'),
               path('publisher',views.publisher,name = 'publisher'),
               path('book',views.book,name = 'book'),]