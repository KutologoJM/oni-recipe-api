from django.urls import path, include
from .views import *

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='Dashboard'),
    path('profile/', ProfileView.as_view(), name='Profile'),
    path("", include("rest_framework.urls")),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    # path('placeholder/', CustomView.as_view(), name='placeholder'),
]
