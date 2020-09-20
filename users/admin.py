from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ custom user admin """

    """
    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("superhost", "language", "currency")
    """

    # 기존필드셋과 커스텀필드셋 추가하기
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

