from django.db import models

# Create your models here.


class Product(models.Model):
    """Model for Product instance"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
