from django.contrib import admin
from .models import User, Order
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom fields', {
            'fields': ('address', 'avatar_img', 'phone_number', 'date_of_birth', ),
        }),
    )

admin.site.register(User,CustomUserAdmin)
admin.site.register(Order)