from django_filters import rest_framework as filters

from notes.models import Note


class NoteFilter(filters.FilterSet):
    parent = filters.CharFilter(
        method='filter_by_parent',
        required=False,
    )

    def filter_by_parent(self, queryset, name, value):
        if value == 'null':
            return queryset.filter(parent__isnull=True)

        if value:
            return queryset.filter(parent__id=value)

        return queryset

    class Meta:
        model = Note
        fields = ['parent']
