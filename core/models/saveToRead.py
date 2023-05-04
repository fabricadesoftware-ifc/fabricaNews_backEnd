from django.db import models
from .user import User
from .news import News


class SaveToRead(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="save_to_reads"
    )
    news = models.ForeignKey(
        News, on_delete=models.PROTECT, related_name="save_to_reads"
    )
