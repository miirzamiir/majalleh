from django.urls import path
from . import views

urlpatterns = [
    path('<int:article_id>', views.single_article, name='article'),
    path('new_article', views.new_article, name='new_article'),
    path('full_width/<int:article_id>', views.full_width, name='full_width')
]
