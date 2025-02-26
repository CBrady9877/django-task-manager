from django.db import models

# Create your models here.
class Task(models.Model): 
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    task_complete = models.BooleanField(default=False)

class Reminders(models.Model):
    reminder_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("dat published")
    
    