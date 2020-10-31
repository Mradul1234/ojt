from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_key = models.CharField(max_length=50, help_text='fill in format: MP for MyProject')
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name

class Task(models.Model):
    PRIORITY = (
                ('High','2'),
                ('Medium','1'),
                ('Low','0'),
                )
    STATUS = (
            ('TO DO','TO DO'),
            ('Done','Done'),
            ('In Progress','In Progress'),
            )

    task_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='+')
    task_number = models.IntegerField() 
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    task_reporter = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+', )
    task_assignee = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    task_created_at = models.DateTimeField(auto_now_add=True)
    task_updated_at = models.DateTimeField(auto_now=True)
    task_deadline_date = models.DateField()
    task_priority =models.CharField(max_length=100, choices=PRIORITY) 
    task_status = models.CharField(max_length=100, choices=STATUS)
    

    @property
    def task_id(self):
        return f"{self.task_project.project_key} - {self.task_number}"

    def __str__(self):
        return self.task_id

class TaskComment(models.Model):

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' comment'



    
