from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'parent', 'created')
    search_fields = ('title', 'owner__username')
    list_filter = ('owner', 'parent', 'created', 'modified')


admin.site.register(Note, NoteAdmin)
