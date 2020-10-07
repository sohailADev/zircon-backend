from django.contrib import admin

from zircon_api.models import InstaGramUser, Post, Notification, Login, Signup
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
                                    'email',

                                ),
                        },
                    ),     
                )

admin.site.register(InstaGramUser,CustomUserAdmin) 
admin.site.register(Post)
admin.site.register(Notification)
admin.site.register(Login)
admin.site.register(Signup)