from django.db import models
from django.contrib.auth import get_user_model
from project.models import Project

CustomUser = get_user_model()

class TeamMember(models.Model):
    full_name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(
        max_length=50,
        choices=[
        ('SEO', 'SEO'),
        ('Development', 'Development'),
        ('UI/UX', 'UI/UX'),
        ],
        blank=True,
        null=True
    )
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_team_members')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    projects = models.ManyToManyField(Project, related_name='assigned_team_members', blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.employee_id})"

    class Meta:
        ordering = ['full_name']