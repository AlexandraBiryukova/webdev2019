from django.db import models

# Create your models here.
class Info(models.Model):
    description=models.TextField(default='INFORMATION')

    def __str__(self):
        return self.description


class HomeObject(models.Model):
    date=models.DateField()
    description=models.TextField(default='')

    def __str__(self):
        return self.date.__str__()+" :::: "+self.description

