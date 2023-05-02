from django.db import models
from .user import User
from .news import News

class Reaction(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    emoji = models.CharField(max_length=300, null=False, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="reactions"
    )
    news = models.ForeignKey(
        News, on_delete=models.PROTECT, related_name="reactions"
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Reaction"
        verbose_name_plural = "Reactions"