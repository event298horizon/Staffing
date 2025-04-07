from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from .forms import JobForm

def landing_page(request):
    return render(request, 'myapp/landing.html')

def find_job(request):
    query = request.GET.get('q')
    jobs = Job.objects.filter(approved = True)
    if query:
        jobs = Job.objects.filter(job_title__icontains=query)
    return render(request, 'myapp/find_job.html', {'jobs': jobs})

def hire_talent(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.approved = False  # pending approval
            job.save()
            return render(request, 'myapp/hire_thanks.html')
    else:
        form = JobForm()
    return render(request, 'myapp/hire_talent.html', {'form': form})