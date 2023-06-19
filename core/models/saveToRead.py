from django.db import models
from user.models import User
from .news import News


class SaveToRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='SaveToReads')
    news = models.ForeignKey(News, on_delete=models.PROTECT, related_name='SaveToReads')
