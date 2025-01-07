from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from notes.api.v1.serializers import NoteSerializer
from notes.models import Note

User = get_user_model()


class TestNoteSerializer(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="TestNoteSerializer",
            password="TestNoteSerializer",
            email="TestNoteSerializer@test.com",
        )

    def test_valid_serializer(self):
        note_1 = Note.objects.create(
            owner=self.user,
            title="Note test_valid_serializer 1",
            content="Content",
        )
        note_2 = Note.objects.create(
            owner=self.user,
            title="Note test_valid_serializer 2",
            content="Content",
        )
        tz = timezone.get_current_timezone()
        data = NoteSerializer([note_1, note_2], many=True).data
        expected_data = [
            {
                "id": note_1.id,
                "owner": self.user.id,
                "title": "Note test_valid_serializer 1",
                "content": "Content",
                "image": None,
                "parent": None,
                "children": [],
                "created": note_1.created.astimezone(tz).isoformat(),
                "modified": note_1.modified.astimezone(tz).isoformat(),
            },
            {
                "id": note_2.id,
                "owner": self.user.id,
                "title": "Note test_valid_serializer 2",
                "content": "Content",
                "image": None,
                "parent": None,
                "children": [],
                "created": note_2.created.astimezone(tz).isoformat(),
                "modified": note_2.modified.astimezone(tz).isoformat(),
            },
        ]
        self.assertEqual(data, expected_data)

    def test_create_children(self):
        note_parent = Note.objects.create(
            owner=self.user,
            title="Note test_create_children parent",
        )
        note_child_1 = Note.objects.create(
            owner=self.user,
            title="Note test_create_children child 1",
            parent=note_parent,
        )
        note_child_2 = Note.objects.create(
            owner=self.user,
            title="Note test_create_children child 2",
            parent=note_parent,
        )

        children = note_parent.children.all()
        self.assertEqual(len(children), 2)
        self.assertIn(children[0].id, (note_child_1.id, note_child_2.id))
        self.assertIn(children[1].id, (note_child_1.id, note_child_2.id))
        self.assertNotEqual(children[0].id, children[1].id)

        data = NoteSerializer(note_parent).data
        children_data = data["children"]
        self.assertEqual(len(children_data), 2)
        self.assertIn(children_data[0]["id"], (note_child_1.id, note_child_2.id))
        self.assertIn(children_data[1]["id"], (note_child_1.id, note_child_2.id))
        self.assertNotEqual(children_data[0]["id"], children_data[1]["id"])
