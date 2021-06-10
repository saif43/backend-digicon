from django.contrib.auth.models import User
from rest_framework import generics, authentication, permissions, mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings
from rest_framework import status, viewsets, filters

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.db.models import Q
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from user import serializers, models
import user


class CreateUserAPIView(generics.CreateAPIView):
    """Creates a new user in the system"""

    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]


class ManageUserView(generics.RetrieveAPIView):
    """Manage the authenticated user"""

    serializer_class = serializers.UserSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """Retrive and return authenticated user"""
        return self.request.user


class CartViewSet(viewsets.ModelViewSet):
    """Viewset for Cart"""

    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
