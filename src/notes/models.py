from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TimeMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Note(TimeMixin):
    owner = models.ForeignKey(
        verbose_name="Note owner",
        to=User,
        related_name="notes",
        on_delete=models.CASCADE,

    )
    title = models.CharField(
        verbose_name="Note title",
        max_length=255,
    )
    content = models.TextField(
        verbose_name="Note content",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        verbose_name="Image for header",
        upload_to="notes/images/",
        blank=True,
        null=True,
    )
    parent = models.ForeignKey(
        verbose_name="Parent note",
        to="self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.owner.username} | {self.title}"
