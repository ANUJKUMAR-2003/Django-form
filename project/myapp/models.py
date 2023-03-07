from django.db import models

year_choices = ['1st','2nd','3rd','4th','5th','6th']
# Create your models here.
class form(models.Model):
    Name = models.CharField( max_length=20)
    email = models.EmailField(max_length=20)
    mobile_number = models.CharField(max_length=10)
    college = models.CharField(max_length=50)
    branch = models.CharField(max_length=30)
    year = models.CharField(max_length=10,choices=year_choices)
    
    def __str__(self):
        return self.Name + '-' + self.branch + '-' + self.year