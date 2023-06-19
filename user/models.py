from django.db import models
from core.models import Project


class User(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

class UserInteractions(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="UserInteractions"
    )
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, related_name="UserInteractions"
    )
    interaction_type = models.CharField(max_length=20, null=False, blank=False)
    interaction_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    has_notification = models.BooleanField(default=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f"{self.interaction_type}"
    
class UserProjectFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_project_follows")
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name="user_project_follows")

    def __str__(self):
        return self.user