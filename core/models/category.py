from django.db import models


class Category(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    user_follow = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f'{self.description}  {self.user_follow}'
