from django.shortcuts import render
from .models import Job, Application

# View for displaying job listings
def job_listings(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/jobs.html', {'jobs': jobs})

# View for displaying applications for a specific job
def job_applications(request, job_id):
    applications = Application.objects.filter(job_id=job_id)
    return render(request, 'jobs/applications.html', {'applications': applications})
