from django.urls import path

from authorization import views

urlpatterns = [
    path('login', views.authorization, name='login'),
    path('register', views.registration, name='register'),
    path('logout', views.logout_user, name='logout'),
]