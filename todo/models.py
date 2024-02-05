from django.db import models


# Create your models here.

class AddTask(models.Model):
    task_name = models.CharField(max_length=100)
    due_date = models.DateField()
    description = models.TextField()
    complete = models.BooleanField(default=False,blank=True,null=True)
    pending = models.BooleanField(default=False,blank=True,null=True)

    class Meta:
        ordering = ['due_date']
