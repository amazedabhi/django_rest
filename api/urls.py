from django.urls import path
from api import views

urlpatterns=[
    path('articles/',views.ArticleListView.as_view()),
    path('articles/<int:pk>',views.ArticleDetailView.as_view())
]