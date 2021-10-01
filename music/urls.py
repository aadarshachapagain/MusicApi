
from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('api/', api.music_list.as_view()),
    path('api/<int:pk>/', api.music_detail.as_view()),
]