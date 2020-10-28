from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User

# Register your models here.

class Admin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            _("Personal info"),
            {"fields": ("type_id", "personal_code", "personal_id", "first_name", "last_name",
                        "telephone", "address")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "is_superuser",
                    "is_staff",
                ),
            },
        ),
    )
    list_display = ("id", "username", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("username",)

admin.site.register(User, Admin)