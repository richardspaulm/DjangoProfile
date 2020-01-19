from django.contrib import admin

from .models import Genre, Project, ProjectInstance, Language

# Register your models here.
admin.site.register(Genre)
admin.site.register(Project)
admin.site.register(ProjectInstance)
admin.site.register(Language)
