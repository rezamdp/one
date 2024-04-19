from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.add_fieldsets += (
    (
        "فیلد سفارشی",
        {
            "classes": ("wide",),
            "fields": ("is_verified", "phone_number"),
        },
    ),
)
UserAdmin.list_display += ("is_verified" ,"phone_number",'imgs_tag')

UserAdmin.fieldsets += (
        ('فیلد سفارشی', {"fields": ("is_verified", "phone_number", "image_user")}),
        )

admin.site.register(User, UserAdmin)