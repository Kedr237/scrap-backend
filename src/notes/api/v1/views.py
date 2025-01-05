from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from notes.models import Note

from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    '''Needs "Authorization" header in format: Bearer {token}'''
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete']

    def perform_create(self, serializer: NoteSerializer):
        serializer.save(owner=self.request.user)
