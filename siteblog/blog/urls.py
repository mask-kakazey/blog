from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/', get_category, name='category'),
    path('category/<str:title>/', PostByCategory.as_view(), name='one_category'),
    path('post/<str:slug>/', get_post, name='post'),
]
