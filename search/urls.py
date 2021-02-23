from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('tags', views.tags, name='tags'),
    path('category', views.category, name='category')
]
