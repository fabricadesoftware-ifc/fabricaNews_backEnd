from django.db import models
from .user import User
# from .news import News

class Comments(models.Model):
    comment = models.CharField(max_length=5000, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="comments")
    # news = models.ForeignKey(News, on_delete=models.PROTECT, related_name="comments")
    
    def __str__(self):
        return self.comment