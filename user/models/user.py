from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"
    