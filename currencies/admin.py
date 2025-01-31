from django.contrib import admin
from .models import Currency
from .services import update_currency_rates

# Register your models here.

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'rate_to_usd', 'updated_at']
    actions = ['update_rates']

    def update_rates(self, request, queryset):
        success, message = update_currency_rates()
        if success:
            self.message_user(request, message)
        else:
            self.message_user(request, f"Error: {message}", level='ERROR')
    update_rates.short_description = "Actualizar tasas desde la API"