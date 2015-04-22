import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class SystemRole(models.Model):
    role_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.role_name


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role_id = models.ForeignKey(SystemRole)

    def __str__(self):
        return self.username


class DTable(models.Model):
    
    TABLE_STATUSES = (
            ('u','InUsed'),
            ('o','Vacant'),
            ('r','Reserved'),
    )
    status = models.CharField(max_length=1,choices=TABLE_STATUSES)
    description = models.CharField(max_length=200)
    capacity = models.IntegetField(default=2)
    main_table = models.ForeignKey(DTable)

    def __str__(self):
        return self.description


