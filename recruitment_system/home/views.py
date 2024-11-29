from django.views.generic import (
    ListView,DetailView
)
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
import re   
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from job_posts.models import Job
from applications.models import Application, Applicant

# Create your views here.


class WebHomeView(ListView):
    model = Job
    template_name = 'home/home.html'
    context_object_name = 'jobs'
    
    def get_queryset(self): 
        return Job.objects.filter(job_status=True).select_related('company').order_by('-posted_date')[:5]
    
class JobListView(ListView):
    model = Job
    template_name = 'home/job-list.html'
    context_object_name = 'jobs'
    paginate_by = 10

    def get_queryset(self):
        # Base queryset of active, non-expired jobs
        queryset = Job.objects.filter(job_status=True).select_related('company')

        # Search and filter functionality
        query = self.request.GET.get('q')
        job_level = self.request.GET.get('job_level')
        employment_type = self.request.GET.get('employment_type')
        location = self.request.GET.get('location')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | 
                Q(job_function__icontains=query) | 
                Q(company__name__icontains=query)
            )
        
        if job_level:
            queryset = queryset.filter(job_level=job_level)
        
        if employment_type:
            queryset = queryset.filter(employment_type=employment_type)
        
        if location:
            queryset = queryset.filter(location__icontains=location)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_levels'] = Job.JOB_LEVEL_CHOICES
        context['employment_types'] = Job.EMPLOYMENT_TYPE_CHOICES
        
        # Get all location values as a flat list
        distinct_locations = Job.objects.values_list('location', flat=True)
    
        # Use a set to store unique values for efficiency
        unique_locations = set()
        
    
        # Process each location
        for location in distinct_locations:
            # Normalize: uppercase and strip whitespace
            location = location.lower().strip()
            
            # Split by common delimiters (/, -, ,, or whitespace)
            parts = re.split(r'[,\s/-]+', location)
            
            # Add each part to the unique set
            unique_locations.update(parts)
    
        # Convert the set to a sorted list and assign it to the context
        locations = {item.capitalize() for item in unique_locations}
        context['distinct_locations'] = sorted(locations)
    
        return context
    
    def post(self, request, *args, **kwargs):
        try:
            job_id = request.POST.get("job_id")
            if not job_id:
                messages.error(request, "Job ID is required")
                return HttpResponseRedirect(reverse('home-job-list'))
    
            job = get_object_or_404(Job, id=job_id)
            applicant = get_object_or_404(Applicant, user=request.user)
    
            # Check for existing application first
            existing_application = Application.objects.filter(
                job=job,
                applicant=applicant
            ).exists()
    
            if existing_application:
                messages.warning(request, f"You have already applied for {job.title}")
            else:
                # Create new application
                Application.objects.create(
                    job=job,
                    applicant=applicant
                )
                messages.success(request, f"Successfully applied for {job.title}")
    
            return HttpResponseRedirect(reverse('home-job-list'))

        except Applicant.DoesNotExist:
            messages.error(request, "You need to complete your applicant profile first")
            return HttpResponseRedirect(reverse('application-home'))
        except Exception as e:
            messages.error(request, f"An error occurred while processing your application: {str(e)}")
            return HttpResponseRedirect(reverse('home-job-list'))
        
        
        
        
class DetailJob(DetailView):
    model = Job
    template_name = 'home/job-detail.html'
    context_object_name = 'job'