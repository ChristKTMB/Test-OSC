from django.urls import path
from .views import ArticlesListCreate, ArticlesRetrieveUpdateDestroy

urlpatterns = [
    path('articles/', ArticlesListCreate.as_view(), name='articles-list-create'),
    path('articles/<int:pk>/', ArticlesRetrieveUpdateDestroy.as_view(), name='articles-retrieve-update-destroy'),
]
