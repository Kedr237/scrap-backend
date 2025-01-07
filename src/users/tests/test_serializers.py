from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase

from users.serializers import UserSerializer

User = get_user_model()


class TestUserSerializer(TestCase):
    def test_valid_serializer(self):
        user = User.objects.create_user(
            username="test_valid_serializer",
            password="test_valid_serializer",
            email="test_valid_serializer@test.com",
        )
        data = UserSerializer(user).data

        self.assertEqual(data["username"], user.username)
        self.assertEqual(data["email"], user.email)
        self.assertNotIn("password", data)
        self.assertTrue(user.check_password("test_valid_serializer"))

    def test_repetitive_username(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username="test_repetitive_username",
                password="test_repetitive_username_1",
                email="test_valid_serializer_1@test.com",
            )
            User.objects.create_user(
                username="test_repetitive_username",
                password="test_repetitive_username_2",
                email="test_valid_serializer_2@test.com",
            )

    def test_repetitive_email(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username="test_repetitive_email_1",
                password="test_repetitive_email_1",
                email="test_repetitive_email@test.com",
            )
            User.objects.create_user(
                username="test_repetitive_email_2",
                password="test_repetitive_email_2",
                email="test_repetitive_email@test.com",
            )
