from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# admin.site.register(models.User, CustomUserAdmin)
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custum User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
    # list_display = ('username', 'gender', 'language', 'currency', 'superhost')
    # list_filter = ("language", "currency", "superhost",)
