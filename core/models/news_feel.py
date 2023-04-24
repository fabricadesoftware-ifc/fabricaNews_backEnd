from django.db import models
from .user import User
from .news import News
from .feeling import Feeling

class NewsFeel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="news_feels"
    )
    news = models.ForeignKey(
        News, on_delete=models.PROTECT, related_name="news_feels"
    )
    feeling = models.ForeignKey(
        Feeling, on_delete=models.PROTECT, related_name="news_feels"
    )

    def __str__(self):
        return f"{self.user} {self.feeling}"
        {self.news}