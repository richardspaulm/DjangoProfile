from django.shortcuts import render
from django.views import generic
# Create your views here.
from webresume.models import Project, ProjectInstance, Genre
from django.shortcuts import get_object_or_404

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_projects = Project.objects.all().count()
    num_instances = ProjectInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_completed = ProjectInstance.objects.filter(stat__exact='C').count()    
    context = {
        'num_projects': num_projects,
        'num_instances': num_instances,
        'num_instances_completed': num_instances_completed
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class ProjectDetailView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        context = {'project': project}
        return render(request, 'projects/project_detail.html', context)

class GenreListView(generic.ListView):
    def get(self, request, *args, **kwargs):
        genre = Genre.objects.filter(pk=kwargs['pk'])
        project = Project.objects.filter(genre__in=genre)
        context = {'project': project, 'genre': genre}
        return render(request, 'subjects/subject_list.html', context)



class ProjectListView(generic.ListView):
    model = Project
    context_object_name = "my_project_view"
    queryset = Project.objects.all()
    template_name = "projects/project_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
