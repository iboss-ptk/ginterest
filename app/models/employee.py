from django.db import models

class EmployeeModel(models.Model):
    CHEF = 'c'
    EMPLOYEE_ROLES = (
        ('m','Manager'),
        (CHEF,'Chef'),
        ('w','WaitingStaff'),
        ('s','Staff'),
        ('t','Trainee'),
    )
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    home_tel_no = models.CharField(max_length=9)
    mobile_no = models.CharField(max_length=10)
    pic_path = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    role = models.CharField(max_length=1,choices=EMPLOYEE_ROLES)

    def __str__(self):
        return self.firstname+" "+self.lastname+" ["+self.role+"]"

    def is_chef(self):
        return self.role in self.CHEF