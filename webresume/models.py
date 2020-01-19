from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length = 200, help_text="Enter Subject Area (Machine Learning)")
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=2000)
    genre = models.ManyToManyField(Genre)
    language = models.ManyToManyField(Language)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])

import uuid

class ProjectInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
    STATUS = (
        ('C', 'Completed'),
        ('P', 'In Progress')
    )
    stat = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='C',
        help_text="Project Status"
    )
    def __str__(self):
        return f'{self.id} ({self.project.title})'
