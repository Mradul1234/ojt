from django.contrib import admin
from .models import Project, Task, TaskComment

# Register your models here.
admin.site.register(Project)

admin.site.register(TaskComment)

class TaskAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["task_reporter", "task_created_at"]
        else:
            return []

admin.site.register(Task, TaskAdmin)