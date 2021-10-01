
from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('api/', api.genre_list.as_view()),
    path('api/<int:pk>/', api.genre_detail.as_view()),
]