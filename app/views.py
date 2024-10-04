
# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Task, TaskList

from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html')  # Create a home.html template

# class LogoutView():
#     def get(self, request):
#         logout(request)
#         return redirect('login') 



def dashboard_view(request):
    task_lists = TaskList.objects.all()
    total_tasks = Task.objects.count()
    ongoing_tasks = Task.objects.filter(status='ongoing').count()
    completed_tasks = Task.objects.filter(status='completed').count()
    overdue_tasks = Task.objects.filter(status='overdue').count()

    # Calculate percentage of completed tasks
    if total_tasks > 0:
        progress_percentage = (completed_tasks / total_tasks) * 100
    else:
        progress_percentage = 0

    # Get tasks that are upcoming (today or in the future)
    upcoming_tasks = Task.objects.filter(due_date__gte=timezone.now().date()).order_by('due_date')

    context = {
        'task_lists': task_lists,
        'total_tasks': total_tasks,
        'ongoing_tasks': ongoing_tasks,
        'completed_tasks': completed_tasks,
        'overdue_tasks': overdue_tasks,
        'progress_percentage': progress_percentage,
        'upcoming_tasks': upcoming_tasks,
    }

    return render(request, 'dashboard.html', context)

