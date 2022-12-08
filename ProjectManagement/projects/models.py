from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
            ('1', 'Pending'),
            ('2', 'In Progress'),
            ('3', 'Done')
        )
    
DUE =   (
            ('1', 'On Due'),
            ('2', 'Overdue'),
            ('3', 'Done'),
        )



class Project(models.Model):
# each class variable represents a database i.e. table field in the model

    
    name = models.CharField(max_length=200)
    assign = models.ManyToManyField(User)
    description = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)
    date_created = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)
    dead_line = models.DateTimeField('dead line')
    company = models.ForeignKey('register.Company', on_delete=models.CASCADE, default='1')
    complete_per = models.FloatField(max_length=3, validators = [MinValueValidator(0), MaxValueValidator(100)])
    
    class Meta:
        ordering = ['name', 'dead_line', 'complete_per']
    
    def __str__(self):
        return self.name


class Task(models.Model):
    
    task_name = models.CharField(max_length=80)
    assign = models.ManyToManyField(User)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS, default=1)
    due = models.CharField(max_length=7, choices=DUE, default=1)
    
    
    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)