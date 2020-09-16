from django.urls import path
from api import views

urlpatterns=[
    path('',views.usersApi),
    path('articles',views.articleApi),
]