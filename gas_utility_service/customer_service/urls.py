from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
    path('support/', views.support_dashboard, name='support_dashboard'),
    path('signup/', views.signup, name='signup'),
     path('profile/', views.profile, name='profile'),
     path('view/<int:request_id>/', views.view_request, name='view_request'),
     path('', views.services, name='services'),
     
]
