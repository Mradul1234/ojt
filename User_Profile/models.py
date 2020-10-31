from django.db import models
from django.contrib.auth.models import User
from task_manager.models import Project
 

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.user.username
 
 
