# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

from .models import Project


# Create your views here.

def index(request):
    # return HttpResponse("You're at the projects index.")
    last_updated_projects = Project.objects.order_by('-upd_date')[:15] #displays 15 projects that were updated last
    context = {'last_updated_projects': last_updated_projects}
    return render(request, 'projects/index.html', context)



def show(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'projects/show.html', {'project': project})
