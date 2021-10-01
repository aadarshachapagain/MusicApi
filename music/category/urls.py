
from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('api/', api.category_list.as_view()),
    path('api/<int:pk>/', api.category_detail.as_view()),
]