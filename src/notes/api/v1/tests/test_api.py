from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from notes.models import Note

User = get_user_model()


class TestNoteView(APITestCase):
    def setUp(self):
        self.login_data = {
            "username": "TestNoteView",
            "password": "TestNoteView",
            "email": "TestNoteView@test.com",
        }
        self.user = User.objects.create_user(**self.login_data)
        self.url_list = "notes-list"
        self.url_detail = "notes-detail"

    def authenticate(self):
        token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

    def test_post_note_auth(self):
        self.authenticate()
        data = {
            "title": "Note test_post_note_auth",
            "content": "Content",
        }

        response = self.client.post(reverse(self.url_list), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_note = Note.objects.filter(title=data["title"])
        self.assertTrue(created_note.exists())

    def test_post_note_unauth(self):
        self.client.logout()
        data = {
            "title": "Note test_post_note_unauth",
            "content": "Content",
        }

        response = self.client.post(reverse(self.url_list), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        created_note = Note.objects.filter(title=data["title"])
        self.assertFalse(created_note.exists())

    def test_get_notes(self):
        self.authenticate()
        Note.objects.create(title="Note", owner=self.user)
        Note.objects.create(title="Note", owner=self.user)

        response = self.client.get(reverse(self.url_list))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_get_note(self):
        self.authenticate()
        note = Note.objects.create(title="Note", owner=self.user)
        url_detail = reverse(self.url_detail, args=[note.id])

        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], note.id)

    def test_patch_note(self):
        self.authenticate()
        note = Note.objects.create(title="Note", owner=self.user)
        url_detail = reverse(self.url_detail, args=[note.id])
        updated_data = {"content": "Content"}

        response = self.client.patch(url_detail, data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        note.refresh_from_db()
        self.assertEqual(note.title, "Note")
        self.assertEqual(note.content, updated_data["content"])

    def test_put_note(self):
        self.authenticate()
        note = Note.objects.create(title="Note", owner=self.user)
        url_detail = reverse(self.url_detail, args=[note.id])
        updated_data = {"title": "Note", "content": "Content"}

        response = self.client.put(url_detail, data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_note(self):
        self.authenticate()
        note = Note.objects.create(title="Note", owner=self.user)
        url_detail = reverse(self.url_detail, args=[note.id])

        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        deleted_note = Note.objects.filter(id=note.id)
        self.assertFalse(deleted_note.exists())

    def test_post_child_note(self):
        self.authenticate()
        parent_note = Note.objects.create(
            owner=self.user,
            title="Note test_post_child_note 1",
            content="Content",
        )
        data = {
            "title": "Note test_post_child_note 2",
            "content": "Content",
            "parent": parent_note.id,
        }

        response_post = self.client.post(reverse(self.url_list), data)
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        url_detail = reverse(self.url_detail, args=[parent_note.id])
        response_get = self.client.get(url_detail)
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_get.data["id"], parent_note.id)
        self.assertEqual(response_get.data["children"][0]["title"], data["title"])
