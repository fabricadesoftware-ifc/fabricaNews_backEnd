from django.db import models
from user.models.user import User


class Project(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="projects")

    def __str__(self):
        return f"{self.title}"
