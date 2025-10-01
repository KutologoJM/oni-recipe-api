from django.views.generic import *
from rest_framework import generics
from django.contrib.auth.models import User
from .permissions import IsNotAuthenticated
from .serializers import *

# Create your views here.


class DashboardView(TemplateView):
    template_name = "accounts/Dashboard.html"


class ProfileView(TemplateView):
    template_name = "accounts/Profile.html"


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [IsNotAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
