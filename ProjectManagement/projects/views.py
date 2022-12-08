# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from django.db.models import Avg
from register.models import Project
from projects.models import Task
from projects.forms import TaskRegistrationForm
from projects.forms import ProjectRegistrationForm
# from projects.forms import ProjectUpdateForm

from .models import Project


# Create your views here.

def projects(request):
    projects = Project.objects.all()
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    tasks = Task.objects.all()
    overdue_tasks = tasks.filter(due='2')
    context = {
        'avg_projects' : avg_projects,
        'projects' : projects,
        'tasks' : tasks,
        'overdue_tasks' : overdue_tasks,
    }
    return render(request, 'projects/projects.html', context)

def newTask(request):
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            # return render(request, 'dashboard/', context)
            return render(request, 'projects/new_task.html', context)
        else:
            return render(request, 'projects/new_task.html', context)
    else:
        form = TaskRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_task.html', context)

def newProject(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = ProjectRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_project.html', context)
        else:
            return render(request, 'projects/new_project.html', context)
    else:
        form = ProjectRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_project.html', context)


# def fetchProject(request, project_id)
#     user = Project.objects.get(id=project_id)
    

        
        
# def editProject(request, project_id):
#     project = Project.objects.get(id=project_id)
#     form = ProjectUpdateForm(request.POST, request.FILES)
#     if request.method == 'POST':
#         context = {'form': form}
#         if form.is_valid():
#             project.name = form.cleaned_data.get("name")
#             form.save()
#             updated = True
#             form = ProjectRegistrationForm()
#             context = {
#                 'updated': updated,
#                 'form': form,
#             }
#             return render(request, 'projects/edit_project.html', context)
#         else:
#             return render(request, 'projects/edit_project.html', context)
#     else:
#         form = ProjectRegistrationForm()
#         context = {
#             'form': form,
#         }
#         return render(request,'projects/edit_project.html', context)

