from django.db import models

from user.models import User

from .news import News


class Reaction(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    emoji = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Reaction"
        verbose_name_plural = "Reactions"
