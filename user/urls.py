from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.register_view, name='register_view'),
    path('sign_in/', views.sign_in_view, name='sign_in_view'),
    path('logout/', views.logout_view, name='logout_view'),
]