from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class myform(models.Model):
    Name = models.CharField( max_length=20)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    college = models.CharField(max_length=50)
    branch = models.CharField(max_length=30)
    year = models.CharField(max_length=10)
    
    def __str__(self):
        return self.Name + '-' + self.branch + '-' + self.year