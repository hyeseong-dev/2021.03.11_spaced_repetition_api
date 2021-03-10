from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email','is_admin')
    pass

admin.site.register(User, UserAdmin)