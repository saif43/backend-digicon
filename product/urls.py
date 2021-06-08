from django.urls import path, include
from product import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.ProductViewSet)

app_name = "product"


urlpatterns = [
    path("", include(router.urls)),
]
