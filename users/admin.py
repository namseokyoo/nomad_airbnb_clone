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
            }
        ),
    )
    # list_display = ('username', 'gender', 'language', 'currency', 'superhost')
    # list_filter = ("language", "currency", "superhost",)
