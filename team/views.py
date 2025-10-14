from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import TeamMember
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

@login_required
def team(request):
    team_members = TeamMember.objects.all()
    total_projects = TeamMember.objects.aggregate(total_projects=Count('projects'))['total_projects'] or 0
    distinct_departments = TeamMember.objects.values('department').distinct().count()
    return render(request, 'team.html', {
        'team_members': team_members,
        'total_projects': total_projects,
        'distinct_departments': distinct_departments
    })

@login_required
def create_team_member(request):
    if request.method == 'POST':
        full_name = request.POST.get('employeeName')
        employee_id = request.POST.get('employeeId')
        designation = request.POST.get('designation')
        department = request.POST.get('department')

        if not all([full_name, employee_id, designation]):
            messages.error(request, 'Please fill all required fields.')
            return redirect('team:team')

        try:
            TeamMember.objects.create(
                full_name=full_name,
                employee_id=employee_id,
                designation=designation,
                department=department if department else None,
                created_by=request.user
            )
            messages.success(request, 'Team member added successfully!')
            return redirect('team:team')
        except Exception as e:
            messages.error(request, f'Error adding team member: {str(e)}')
            return redirect('team:team')

    return redirect('team:team')