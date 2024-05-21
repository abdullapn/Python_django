from django.shortcuts import render,redirect
from . import forms,models
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.conf import settings
from .models import Tasks
from . forms import TasksForm

def home_view(request):
    return render(request, 'ecom/index.html')


def admin_task_view(request):
    tasks = Tasks.objects.all()
    return render(request,'admin_tasks.html',{'tasks': tasks})


def afterlogin_views(request):
    return redirect('admin-task')

# Create your views here. 

def admin_add_tasks_view(request):
    if request.method == 'POST':
        tasksForm = TasksForm(request.POST)  # Corrected variable name
        if tasksForm.is_valid():
            tasksForm.save()
            return HttpResponseRedirect('/admin-tasks')
    else:    
        tasksForm = TasksForm()
    return render(request, 'admin_add_tasks.html', {'tasksForm': tasksForm})


def index(request):
    return render(request,'index.html')


def loginview(request):
    return render(request,'Login.html')


def registerview (request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydic={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('Login')
    return render(request,'register.html',context=mydic)  


def delete_tasks_view(request,pk):
     tasks=models.Tasks.objects.get(id=pk)
     tasks.delete()
     return redirect('admin-tasks') 

def update_tasks_view(request,pk):
    tasks=models.Tasks.objects.get(id=pk)
    tasksForm=forms.TasksForm(instance=tasks)
    if request.method=='POST':
        tasksForm=forms.TasksForm(request.POST,request.FILES,instance=tasks)
        if tasksForm.is_valid():
            tasksForm.save()
            return redirect('admin-tasks')
    return render(request,'admin_update_tasks.html',{'tasksForm':tasksForm})







           
           

