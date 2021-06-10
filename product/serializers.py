from rest_framework import serializers
from product import models
from user import models as userModel


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product"""

    class Meta:
        model = models.Product
        fields = "__all__"
        read_only_fields = ["id"]

    def to_representation(self, instance):
        response = super().to_representation(instance)

        try:
            requested_user = self.context["request"].user
            cart = userModel.Cart.objects.filter(user=requested_user, product=instance)

            if len(cart):
                response["added_to_cart"] = True
            else:
                response["added_to_cart"] = False

        except:
            response["added_to_cart"] = None

        return response
