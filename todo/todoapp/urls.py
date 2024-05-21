from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [

    path('',views.index),
    path('Register',views.registerview),
    path('Login',LoginView.as_view(template_name='login.html'),name='Login'),
    path('accounts/profile/',views.afterlogin_views,name='afterlogin'),
    path('admin-task',views.admin_task_view,name='admin-task'),
    path('admin-tasks', views.admin_task_view,name='admin-tasks'),
    path('admin-add-tasks', views.admin_add_tasks_view,name='admin-add-tasks'),
    path('delete-tasks-<int:pk>',views.delete_tasks_view,name='delete-tasks'),
    path('update-tasks-<int:pk>',views.update_tasks_view,name='update-tasks'),
]