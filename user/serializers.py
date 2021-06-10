from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
import product
from user import models
from product import serializers as productSerializer, models as productModel


class UserSerializer(serializers.ModelSerializer):

    """Serializer for the User object"""

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "name",
            "password",
            "created_timestamp",
        ]

        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 5,
                "style": {"input_type": "password"},
            }
        }
        read_only_fields = ["id", "created_timestamp"]

    def create(self, validated_data):
        """creates user with encrypted password and retruns the user"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class CartSerializer(serializers.ModelSerializer):
    """Serializer for Cart"""

    class Meta:
        model = models.Cart
        fields = "__all__"
        read_only_fields = ["id"]

    def to_representation(self, instance):
        response = super().to_representation(instance)

        product = productModel.Product.objects.get(id=response["product"])

        response["product"] = productSerializer.ProductSerializer(product).data
        response["product"].pop("added_to_cart")

        return response
