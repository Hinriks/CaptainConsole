from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('profile', views.view_profile, name="profile"),
    path('profile/edit', views.edit_profile, name="edit_profile"),
    path('profile/update', views.update_user, name="update_user"),
    path('signup', views.signup_view, name='signup'),
    path('', include('django.contrib.auth.urls')),
]
