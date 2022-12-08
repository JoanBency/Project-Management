from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'projects'

urlpatterns = [
    # /projects/
    path('', views.projects, name='projects'),
    # /projects/id e.g. /projects/1
    path('new-project/', views.newProject, name='new-project'),
    path('new-task/', views.newTask, name='new-task'),
    # path('edit-project/<int:project_id>/', views.editProject, name='edit-project'),
]
