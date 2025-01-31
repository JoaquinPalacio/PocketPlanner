import requests
from django.conf import settings
from .models import Currency

def update_currency_rates():
    api_key = settings.EXCHANGERATE_API_KEY
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza error si hay HTTP error
        data = response.json()
        
        if data.get('result') == 'success':
            for code, rate in data['conversion_rates'].items():
                Currency.objects.update_or_create(
                    code=code,
                    defaults={
                        'name': code,
                        'rate_to_usd': rate,
                    }
                )
            return True, "Tasas actualizadas correctamente."
        else:
            return False, f"Error en la API: {data.get('error-type', 'Unknown error')}"
            
    except requests.exceptions.RequestException as e:
        return False, f"Error de conexión: {str(e)}"