from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user import models
from django.utils.translation import gettext as _

# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["username", "name"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (
            _("Permissons"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important_dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("username", "password1", "password2")},
        ),
    )


# admin.site.register(models.User, UserAdmin)
