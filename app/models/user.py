from django.db import models
from app.models import SystemRoleModel

class UserModel(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role_id = models.ForeignKey(SystemRoleModel)

    def __str__(self):
        return self.username
