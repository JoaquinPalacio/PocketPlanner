from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from currencies.models import Currency
from currencies.services import update_currency_rates

class CurrencyModelTests(TestCase):
    def test_create_currency(self):
        currency = Currency.objects.create(code="EUR", name="Euro", rate_to_usd=0.85)
        self.assertEqual(currency.code, "EUR")
        self.assertEqual(currency.name, "Euro")
        self.assertEqual(currency.rate_to_usd, 0.85)

class CurrencyViewTests(TestCase):
    def setUp(self):
        self.currency = Currency.objects.create(code="USD", name="US Dollar", rate_to_usd=1.0)

    def test_all_currencies_view(self):
        response = self.client.get(reverse("currencies"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "US Dollar")

    def test_converter_view(self):
        response = self.client.post(
            reverse("converter"),
            {
                "from_currency": "USD",
                "to_currency": "USD",
                "amount": 100,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "RESULT: 100.00")

class CurrencyServiceTests(TestCase):
    def test_update_currency_rates(self):
        success, message = update_currency_rates()
        self.assertTrue(success)
        self.assertIn("Tasas actualizadas correctamente.", message)