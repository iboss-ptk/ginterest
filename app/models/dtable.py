from django.db import models

class DTable(models.Model):
    TABLE_STATUSES = (
            ('u','InUsed'),
            ('o','Vacant'),
            ('r','Reserved'),
    )
    status = models.CharField(max_length=1,choices=TABLE_STATUSES,default='o')
    description = models.CharField(max_length=200)
    capacity = models.IntegerField(default=2)
    main_table = models.ForeignKey('self')

    def __str__(self):
        return str(self.id)+' '+self.description
