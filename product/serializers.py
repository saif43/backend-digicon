from rest_framework import serializers
from product import models


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product"""

    class Meta:
        model = models.Product
        fields = "__all__"
        read_only_fields = ["id"]
