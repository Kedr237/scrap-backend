from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ("short_title", "owner", "parent", "created")
    search_fields = ("title", "owner__username")
    list_filter = ("owner", "parent", "created", "modified")
    readonly_fields = ("created", "modified")

    def short_title(self, obj: Note):
        return obj.title[:20] + ("..." if len(obj.title) > 20 else "")
    short_title.short_description = Note._meta.get_field("title").verbose_name


admin.site.register(Note, NoteAdmin)
