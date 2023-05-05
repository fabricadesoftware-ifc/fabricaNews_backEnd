from django.db import models
from .user import User
from .news import News


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    news = models.ForeignKey(News, on_delete=models.PROTECT, null=False, blank=False)
