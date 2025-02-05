from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser
from categories.models import Category

class CategoryModelTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_create_category(self):
        category = Category.objects.create(name="Food", user=self.user)
        self.assertEqual(category.name, "Food")
        self.assertEqual(category.user, self.user)

class CategoryViewTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client.login(username="testuser", password="testpass123")
        self.category = Category.objects.create(name="Travel", user=self.user)

    def test_all_categories_view(self):
        response = self.client.get(reverse("categories"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Travel")

    def test_create_category_view(self):
        response = self.client.post(
            reverse("categories"), {"name": "Entertainment"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Category.objects.filter(name="Entertainment").exists())