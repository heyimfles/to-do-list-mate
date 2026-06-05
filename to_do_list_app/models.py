from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=255
    )


class Task(models.Model):
    content = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    deadline = models.DateTimeField(
        blank=True,
        null=True
    )

    completion_status = models.BooleanField()

    tags = models.ManyToManyField(
        Tag,
        related_name="tags",
        blank=True,
        null=True,
    )
