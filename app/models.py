from django.db import models

# Create your models here.

class Person(models.Model):
    job = models.CharField(max_length=5)
    date = models.DateField(auto_now_add=False,auto_now=True)
    first_name = models.TextField()
    last_name = models.TextField()
    count = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    




