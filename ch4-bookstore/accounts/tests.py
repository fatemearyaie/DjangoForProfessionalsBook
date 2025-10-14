from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve
from .forms import CostumUserCreationForm
from .views import SignUpView




# Create your tests here.
class CostumUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will', email='will@gmail.com', password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'superadmin', email='superadmin@gmail.com', password = '123456789'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)


class SignUpPageTests(TestCase): # new
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
    def test_signup_form(self): # new
        form = self.response.context.get("form")
        self.assertIsInstance(form, CostumUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")
    def test_signup_view(self): # new
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignUpView.as_view().__name__)