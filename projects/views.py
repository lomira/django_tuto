from django.views import generic

from .models import Project


class IndexView(generic.ListView):
    template_name = "projects/index.html"
    context_object_name = "projectz"

    def get_queryset(self):
        """Return all projects."""
        return Project.objects.all()

class DetailView(generic.DetailView):
    model = Project
    template_name = "projects/detail.html"