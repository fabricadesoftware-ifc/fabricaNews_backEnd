from django.db import models


class Help(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    middleName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return (
            f"{self.name}  {self.middleName} {self.email} {self.phone} {self.message}"
        )
