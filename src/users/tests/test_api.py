from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class TestUserRegistration(APITestCase):
    def setUp(self):
        self.register_url = "register_user"

    def test_register_valid(self):
        payload = {
            "username": "test_register_valid",
            "password": "test_register_valid",
            "email": "test_register_valid@test.com",
        }

        response = self.client.post(reverse(self.register_url), data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.filter(username=payload["username"])
        self.assertTrue(user.exists())

    def test_register_invalid(self):
        payload = {
            "username": "",
            "password": "test_register_invalid",
            "email": "test_register_invalid@test.com",
        }

        response = self.client.post(reverse(self.register_url), data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(username=payload["username"])
        self.assertFalse(user.exists())

    def test_register_repetitive_username(self):
        payload_1 = {
            "username": "test_register_repetitive_username",
            "password": "test_register_repetitive_username",
            "email": "test_register_repetitive_username@test.com",
        }
        payload_2 = {
            "username": "test_register_repetitive_username",
            "password": "test_register_repetitive_username_2",
            "email": "test_register_repetitive_username_2@test.com",
        }

        response_1 = self.client.post(reverse(self.register_url), data=payload_1)
        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)

        response_2 = self.client.post(reverse(self.register_url), data=payload_2)
        self.assertEqual(response_2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response_2.data)


class TestJWTTokens(APITestCase):
    def setUp(self):
        self.user_data = {
            "username": "TestJWTTokens",
            "password": "TestJWTTokens",
            "email": "TestJWTTokens@test.com",
        }
        self.user = User.objects.create_user(**self.user_data)
        self.obtain_url = "token_obtain_pair"
        self.refresh_url = "token_refresh"

    def test_obtain_tokens(self):
        response = self.client.post(
            reverse(self.obtain_url),
            data={
                "username": self.user_data["username"],
                "password": self.user_data["password"],
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data["access"])
        self.assertIsNotNone(response.data["refresh"])

    def test_refresh_token(self):
        response_token = self.client.post(
            reverse(self.obtain_url),
            data={
                "username": self.user_data["username"],
                "password": self.user_data["password"],
            }
        )

        response = self.client.post(
            reverse(self.refresh_url),
            data={"refresh": response_token.data["refresh"]}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data["access"])
        self.assertIsNotNone(response.data["refresh"])

    def test_changing_obtain_tokens(self):
        response_1 = self.client.post(
            reverse(self.obtain_url),
            data={
                "username": self.user_data["username"],
                "password": self.user_data["password"],
            }
        )
        response_2 = self.client.post(
            reverse(self.obtain_url),
            data={
                "username": self.user_data["username"],
                "password": self.user_data["password"],
            }
        )
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response_1.data["access"], response_2.data["access"])
        self.assertNotEqual(response_1.data["refresh"], response_2.data["refresh"])

    def test_changing_refresh_tokens(self):
        response_token = self.client.post(
            reverse(self.obtain_url),
            data={
                "username": self.user_data["username"],
                "password": self.user_data["password"],
            }
        )

        response_1 = self.client.post(
            reverse(self.refresh_url),
            data={"refresh": response_token.data["refresh"]}
        )
        response_2 = self.client.post(
            reverse(self.refresh_url),
            data={"refresh": response_1.data["refresh"]}
        )
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response_1.data["access"], response_2.data["access"])
        self.assertNotEqual(response_1.data["refresh"], response_2.data["refresh"])

    def test_tokens_blacklist(self):
        response_token = self.client.post(
            reverse(self.obtain_url),
            data={
                "username": self.user_data["username"],
                "password": self.user_data["password"],
            }
        )

        response_1 = self.client.post(
            reverse(self.refresh_url),
            data={"refresh": response_token.data["refresh"]}
        )
        response_2 = self.client.post(
            reverse(self.refresh_url),
            data={"refresh": response_token.data["refresh"]}
        )
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.status_code, status.HTTP_401_UNAUTHORIZED)
