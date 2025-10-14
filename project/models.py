from django.db import models
from django.contrib.auth import get_user_model

class Project(models.Model):
    STATUS_CHOICES = [
        ('Planning', 'Planning'),
        ('In Progress', 'In Progress'),
        ('Review', 'Review'),
        ('Completed', 'Completed'),
    ]

    CATEGORY_CHOICES = [
        ('SEO', 'SEO'),
        ('Development', 'Development'),
        ('UI/UX', 'UI/UX'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    manager = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='managed_projects'
    )
    team_members = models.ManyToManyField(
        get_user_model(),
        related_name='projects',
        blank=True
    )
    attachment = models.FileField(upload_to='project_attachments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']