from django.contrib import admin
from .models import Project
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'manager', 'created_at', 'updated_at')
    list_filter = ('category', 'status', 'manager')
    search_fields = ('title', 'description', 'manager__username', 'manager__email', 'manager__first_name', 'manager__last_name')
    filter_horizontal = ('team_members',)
    list_per_page = 25
    date_hierarchy = 'created_at'

    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Details', {
            'fields': ('category', 'status', 'manager', 'team_members', 'attachment')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('manager').prefetch_related('team_members')

admin.site.register(Project, ProjectAdmin)