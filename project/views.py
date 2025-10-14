from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

@login_required
def project_list(request):
    projects = Project.objects.all()
    users = CustomUser.objects.all()
    return render(request, 'project.html', {'projects': projects, 'users': users})

@login_required
def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('projectTitle')
        description = request.POST.get('projectDescription', '')
        category = request.POST.get('category')
        status = request.POST.get('status')
        manager_input = request.POST.get('projectManager')
        team_members_input = request.POST.getlist('teamMembers')  # Changed to getlist
        attachment = request.FILES.get('attachment')

        if not all([title, category, status, manager_input]):
            messages.error(request, 'Please fill all required fields.')
            return redirect('project:project_list')

        try:
            manager = CustomUser.objects.get(username=manager_input)
            project = Project.objects.create(
                title=title,
                description=description,
                category=category,
                status=status,
                manager=manager,
                attachment=attachment
            )

            if team_members_input:
                users = CustomUser.objects.filter(username__in=team_members_input)
                project.team_members.add(*users)

            messages.success(request, 'Project created successfully!')
            return redirect('project:project_list')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid project manager or team member.')
            return redirect('project:project_list')
        except Exception as e:
            messages.error(request, f'Error creating project: {str(e)}')
            return redirect('project:project_list')

    return redirect('project:project_list')