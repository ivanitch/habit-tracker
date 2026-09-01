from django.contrib import admin

from users.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'is_staff', 'is_active')

    exclude = ('password',)

    readonly_fields = ('last_login', 'date_joined')

    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Личная информация', {'fields': ('avatar', 'phone', 'city')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'is_staff', 'is_active'),
        }),
    )

