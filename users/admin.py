from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser
from currencies.models import Currency

class CustomUserAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        """
        Sobrescribe el método save_model para asignar permisos automáticamente.
        """
        super().save_model(request, obj, form, change)

        # Asignar permisos si el usuario es staff
        if obj.is_staff:
            content_type = ContentType.objects.get_for_model(Currency)
            permission = Permission.objects.get(
                codename='can_update_rates',
                content_type=content_type,
            )
            obj.user_permissions.add(permission)

# Registra el modelo CustomUser con el administrador personalizado
admin.site.register(CustomUser, CustomUserAdmin)