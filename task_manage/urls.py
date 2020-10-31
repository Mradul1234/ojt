from django.urls import path
from task_manage import views

urlpatterns=[

    path('', views.home, name='home'),
    path('project/', views.project, name='project'),
    path('task/<str:pk>/', views.task, name='task'),
    path('task_comment/<str:pk>/', views.task_comment, name='task_comment'),
    path('update_task/<str:pk>/', views.update_task, name='update_task')



]