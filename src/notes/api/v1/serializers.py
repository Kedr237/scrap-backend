from rest_framework import serializers

from notes.models import Note


class NoteChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title"]


class NoteSerializer(serializers.ModelSerializer):
    children = NoteChildrenSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ["owner"]
