from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Project(models.Model):
# each class variable represents a database i.e. table field in the model

    STATUS = (
            ('Pending', 'Pending'),
            ('In Progress', 'In Progress'),
            ('Done', 'Done')
        )
    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)
    date_created = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)
    dead_line = models.DateTimeField('dead line')
    complete_per = models.FloatField(max_length=3, validators = [MinValueValidator(0), MaxValueValidator(100)])
    
    
    
def __str__(self):
    return self.name + " - " + self.status
