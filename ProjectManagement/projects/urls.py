from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    # /projects/
    path('', views.index, name='index'),
    # /projects/id e.g. /projects/1
    path('<int:project_id>/', views.show, name='show'),
]
