from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Job
from .forms import JobForm
from .forms import JobApplicationForm

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

def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, approved=True)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return render(request, 'myapp/application_success.html', {'job': job})
    else:
        form = JobApplicationForm()

    return render(request, 'myapp/apply_job.html', {'job': job, 'form': form}) 