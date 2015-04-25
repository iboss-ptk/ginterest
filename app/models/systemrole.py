from django.db import models

class SystemRoleModel(models.Model):
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name
