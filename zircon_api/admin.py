from django.contrib import admin

from zircon_api.models import InstaGramUser, Post, Notification
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field to show on admin',
            {
                'fields': (
                    'full_name',
                    'bio',
                    'phone',
                    'website',
                    'gender',

                ),
            },
        ),
    )


admin.site.register(InstaGramUser, CustomUserAdmin)
admin.site.register(Post)
admin.site.register(Notification)
