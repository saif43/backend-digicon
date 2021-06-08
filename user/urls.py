from django.urls import path, include
from user import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("cart", views.CartViewSet)

app_name = "user"


urlpatterns = [
    path("", include(router.urls)),
    path("me/", views.ManageUserView.as_view(), name="me"),
    path("create/", views.CreateUserAPIView.as_view(), name="create"),
]
