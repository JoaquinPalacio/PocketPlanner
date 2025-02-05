from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser
from currencies.models import Currency
from categories.models import Category
from transactions.models import Transaction
from transactions.forms import TransactionForm

class TransactionModelTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.currency = Currency.objects.create(code="USD", name="US Dollar", rate_to_usd=1.0)
        self.category = Category.objects.create(name="Food", user=self.user)

    def test_create_transaction(self):
        transaction = Transaction.objects.create(
            amount=100.0,
            type_transaction="deposit",
            user=self.user,
            category=self.category,
            currency=self.currency,
        )
        self.assertEqual(transaction.amount, 100.0)
        self.assertEqual(transaction.type_transaction, "deposit")

class TransactionFormTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.currency = Currency.objects.create(code="USD", name="US Dollar", rate_to_usd=1.0)
        self.category = Category.objects.create(name="Food", user=self.user)

    def test_valid_form(self):
        data = {
            "amount": 200.0,
            "type_transaction": "withdrawal",
            "category": self.category.id,
            "currency": self.currency.id,
        }
        form = TransactionForm(data=data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            "amount": -50.0,  # Invalid amount
            "type_transaction": "withdrawal",
            "category": self.category.id,
            "currency": self.currency.id,
        }
        form = TransactionForm(data=data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn("Amount must be positive", form.errors["amount"])

class TransactionViewTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.currency = Currency.objects.create(code="USD", name="US Dollar", rate_to_usd=1.0)
        self.category = Category.objects.create(name="Food", user=self.user)
        self.client.login(username="testuser", password="testpass123")

    def test_transactions_view(self):
        response = self.client.get(reverse("transactions"))
        self.assertEqual(response.status_code, 200)

    def test_create_transaction_view(self):
        response = self.client.post(
            reverse("transactions"),
            {
                "amount": 300.0,
                "type_transaction": "deposit",
                "category": self.category.id,
                "currency": self.currency.id,
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Transaction.objects.filter(amount=300.0).exists())