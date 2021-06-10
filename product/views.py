from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from product import models, serializers
from rest_framework import viewsets

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    """Viewset for Product"""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAuthenticated]
