from django.urls import path
from . import views

urlpatterns = [
    path('list_category/', views.list_and_manage_categories, name='list_and_manage_categories'),
]
