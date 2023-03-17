from django.db import models

# Create your models here.
class myform(models.Model):
    Name = models.CharField( max_length=20)
    email = models.EmailField(max_length=20)
    mobile_number = models.CharField(max_length=10)
    college = models.CharField(max_length=50)
    branch = models.CharField(max_length=30)
    year = models.CharField(max_length=10)
    
    def __str__(self):
        return self.Name + '-' + self.branch + '-' + self.year