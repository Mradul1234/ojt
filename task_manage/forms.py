from django.forms import ModelForm
from .models import Task, Project, TaskComment

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_name','project_key']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class TaskCommentForm(ModelForm):
    class Meta:
        model = TaskComment
        fields = '__all__'



