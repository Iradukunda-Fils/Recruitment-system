from typing import Any
from django.db.models.query import QuerySet
from django.contrib import messages
from django.views.generic import (
    DetailView,ListView,UpdateView,DeleteView,CreateView,TemplateView
)
from authentication.models import CustomUser
from .models import Application
from privileges.permisions import LoginRequiredUser
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.urls import reverse_lazy


# Create your views here.

class Home(TemplateView):
    template_name = 'applications/home.html'
    
class Applications(ListView):
    model = Application
    template_name = 'applications/applications.html'
    context_object_name = 'applications'

    def get_queryset(self):
        # Ensure the user has an associated applicant to avoid potential errors
        if hasattr(self.request.user, 'applications'):
            applicant = self.request.user.applications
            # Filter applications for this specific applicant, not jobs
            return Application.objects.select_related('applicant').filter(applicant=applicant, status='Pending').order_by('-application_date', '-job__application_deadline')
        return Application.objects.none()


class Settings(TemplateView):
    template_name = 'applications/profile_settings.html'



class NotificationView(TemplateView):
    template_name = 'applications/notifications.html'


class Saved(ListView):
    model = Application  # We are working with applications, not jobs.
    template_name = 'applications/applications_saved.html'
    context_object_name = 'applications'
    
    class Saved(ListView):
        model = Application
        template_name = 'applications/applications_saved.html'
        context_object_name = 'applications'
    
        def get_queryset(self):
            if self.request.user.is_authenticated:
                try:
                    applicant = self.request.user.applicant  # Ensure related_name='applicant' exists
                    return Application.objects.select_related('job', 'applicant').filter(
                        applicant=applicant,
                        status='Pending'
                    ).order_by('-submitted_date', '-job__application_deadline')
                except ObjectDoesNotExist:
                    return Application.objects.none()
            return Application.objects.none()


class UpdateApplication(UpdateView):
    model = Application
    template_name = 'applications/applications/application.html'
    fields = ('applicant', 'job', 'cover_letter')
    success_url = reverse_lazy('saved-applications')
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
         
        # app = self.get_object()
        
        
        # job_title = forms.CharField(
        # initial=str(app.job.title),  # Set the initial value to the job's title
        # widget=forms.SelectMultiple(attrs={'readonly': 'readonly',"disabled":True}),
        # )
        
        form.fields['applicant'].disabled = True
        form.fields['job'].disabled = True
        
        # Optional: Add a widget to indicate a read-only field
        form.fields['cover_letter'].widget.attrs.update({'style': 'background-color: lightgray;width:70%'})
        
        # # Optionally, set widgets or other properties
        # form.fields['cover_letter'].widget.attrs.update({'placeholder': 'Optional cover letter text'})
        # form.fields['interview'].widget.attrs.update({'placeholder': 'Optional interview date'})
        
        return form
    def form_valid(self, form):
        """Custom logic for handling the form submission."""
        # Update the status if 'submit' is in POST data
        if self.request.POST.get('submitted') == 'submitted':
            form.instance.status = "Submitted"
            messages.success(self.request, "Application Submitted successfully.")
        # Save the form and show a success message
        else:
            messages.success(self.request, "Application updated successfully.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Handle invalid form submissions."""
        messages.error(self.request, "There was an error updating the application.")
        return super().form_invalid(form)
    
    
class ApplicationDelete(DeleteView):
    model = Application
    template_name = 'applications/applications/application-delete.html'
    context_object_name = 'job'
    success_url = reverse_lazy('saved-applications')
    

    
    
    
        
