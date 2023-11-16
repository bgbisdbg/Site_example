from http import HTTPStatus
from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.models import User, EmailVerification


class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_success(self):
        data = {
            'first_name': 'diman',
            'last_name': 'Kuznetsov',
            'username': 'vavilon12',
            'email': 'dimon123098@bk.ru',
            'password1': 'Qw89op12',
            'password2': 'Qw89op12'

        }

        response = self.client.post(self.path, data)

        username = data['username']

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('user:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )
