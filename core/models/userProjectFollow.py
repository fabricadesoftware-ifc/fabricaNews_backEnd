from django.db import models
from .user import User
from .project import Project


class UserProjectFollow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="user_project_follows"
    )
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, related_name="user_project_follows"
    )

    def __str__(self):
        return f"{self.user}"
