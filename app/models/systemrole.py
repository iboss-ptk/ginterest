from django.db import models

class SystemRole(models.Model):
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name
