from django.db import models

from project.models.project import Project
from user.models.user import User


class UserProjectFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_project_follows")
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name="user_project_follows")

    def __str__(self):
        return self.user
