from django.db import models

# Create your models here.
class ResumeModel(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length = 50)
    tech = models.CharField(max_length=200)
    email = models.EmailField(unique = True)
    photo = models.FileField()
    class Meta:
        db_table = 'resumesInfo'
