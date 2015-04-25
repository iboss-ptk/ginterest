from django.db import models

class DTableModel(models.Model):
    TABLE_STATUSES = (
            ('u','InUsed'),
            ('o','Vacant'),
            ('r','Reserved'),
    )
    status = models.CharField(max_length=1,choices=TABLE_STATUSES)
    description = models.CharField(max_length=200)
    capacity = models.IntegerField(default=2)
    main_table = models.ForeignKey("DTableModel")

    def __str__(self):
        return self.id+" "+self.description
