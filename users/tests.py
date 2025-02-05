from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from currencies.models import Currency

class CustomUserTests(TestCase):
    def setUp(self):
        self.currency = Currency.objects.create(code="USD", name="US Dollar", rate_to_usd=1.0)

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            password="testpass123",
            first_name="Test",
            last_name="User",
            base_currency=self.currency,
        )
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("testpass123"))
        self.assertEqual(user.base_currency, self.currency)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="admin", password="admin123"
        )
        self.assertEqual(admin_user.username, "admin")
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)

    def test_signup_view(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "newuser",
                "password1": "testpass123",
                "password2": "testpass123",
                "first_name": "New",
                "last_name": "User",
                "base_currency": self.currency.id,
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertTrue(get_user_model().objects.filter(username="newuser").exists())

    def test_login_view(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        response = self.client.post(
            reverse("login"),
            {"username": "testuser", "password": "testpass123"},
        )
        self.assertEqual(response.status_code, 302)  # Redirect after login
        self.assertTrue(user.is_authenticated)