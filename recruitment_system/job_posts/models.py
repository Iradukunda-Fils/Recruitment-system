from django.db import models
from companies.models import Company,Branch
from django.utils import timezone

# Create your models here.

class Job(models.Model):
    EDUCATION_CHOICES = [
        ('No Degree', 'No Degree'),
        ('O Level', 'O Level'),
        ('High School Diploma', 'High School Diploma'),
        ('Bachelor’s Degree', 'Bachelor’s Degree'),
        ('Master’s Degree', 'Master’s Degree'),
        ('PhD or Doctorate', 'PhD or Doctorate'),
    ]
    
    EMPLOYMENT_TYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    ]
    
    JOB_LEVEL_CHOICES = [
        ('Entry Level', 'Entry Level'),
        ('Mid-Senior Level', 'Mid-Senior Level'),
        ('Senior Level', 'Senior Level'),
    ]
    
    # Fields
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=200)
    job_level = models.CharField(max_length=50, choices=JOB_LEVEL_CHOICES, default='Entry Level')
    job_function = models.CharField(max_length=50)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPE_CHOICES, default='Full-time')
    location = models.CharField(max_length=255)
    education = models.CharField(max_length=50, choices=EDUCATION_CHOICES, default='No Degree')
    salary = models.DecimalField(max_digits=12, decimal_places=2,default=00.00)  # Adjusted for currency

    # Additional job details
    description = models.TextField()
    requirements = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField()
    job_status = models.BooleanField(default=False)
    
    
    @property
    def is_active(self):
        return self.job_status
    
    @property
    def is_expired(self):
        return self.application_deadline < timezone.now()
    
    @property
    def applied(self):
        return self.jobs

    
    def __str__(self):
        return f"{self.title} at {self.company.name}"
    
    class Meta:
        ordering = ['-posted_date',]