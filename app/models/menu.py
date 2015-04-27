from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    pic_path = models.ImageField(upload_to='pictures/',default='pictures/no-img.jpg')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
