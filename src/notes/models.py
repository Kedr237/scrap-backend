from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TimeMixin(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation date",
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Change date",
    )

    class Meta:
        abstract = True


class Note(TimeMixin):
    owner = models.ForeignKey(
        to=User,
        related_name="notes",
        on_delete=models.CASCADE,
        verbose_name="Note owner",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Note title",
    )
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name="Note content",
    )
    image = models.ImageField(
        upload_to="notes/images/",
        blank=True,
        null=True,
        verbose_name="Header image",
    )
    parent = models.ForeignKey(
        to="self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
        verbose_name="Parent note",
    )

    def __str__(self):
        return f"{self.owner.username} | \
            {self.title[:20] + ('...' if len(self.title) > 20 else '')}"
