from django.db import models
from django.utils import timezone

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from product import models as productModel
import product


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_kwargs):
        """Creates and saves an user"""
        if not username:
            raise ValueError("User must have an username")

        user = self.model(username=username, **extra_kwargs)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Creates and saves a superuser"""
        user = self.create_user(username=username, password=password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""

    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_timestamp = models.DateTimeField(default=timezone.now, editable=False)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username


class Cart(models.Model):
    """model for cart"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    product = models.ForeignKey(productModel.Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            "user",
            "product",
        )
