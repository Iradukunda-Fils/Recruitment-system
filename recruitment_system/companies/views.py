from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from privileges.permisions import  LoginRequiredCompany
from django.urls import reverse_lazy,reverse
from .models import (
    Branch, CompanyInfo,Employee,
)
from django.views.generic.edit import CreateView
from django.views.generic import (
    DetailView,ListView,UpdateView,DeleteView,CreateView,TemplateView
)
from job_posts.models import Job
from .forms import EmployeeForm
from django.views import View
from django.contrib import messages


# Create your views here.

class Home(LoginRequiredCompany, TemplateView):
      template_name = 'companies/home.html'
      login_url = reverse_lazy('login')

class ManageUsers(LoginRequiredCompany, TemplateView):
    template_name = 'companies/manage_users.html'
    login_url = reverse_lazy('login')

class Analytics(LoginRequiredCompany, TemplateView):
    template_name = 'companies/analytics.html'
    login_url = reverse_lazy('login')


class Settings(LoginRequiredCompany, TemplateView):
    template_name = 'companies/settings.html'
    login_url = reverse_lazy('login')


class JobList(LoginRequiredCompany, ListView):
    model = Job
    template_name = 'companies/job-list.html'
    context_object_name = 'jobs'
    ordering = []
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
        # Ensure the user has an associated company to avoid potential errors
        if hasattr(self.request.user, 'company'):
            return Job.objects.filter(company=self.request.user.company).order_by('-posted_date', '-application_deadline')
        return Job.objects.none()
    
    def post(self, request, *args, **kwargs):
        return redirect('job-create')

class UpdateJob(LoginRequiredCompany, UserPassesTestMixin, UpdateView):
    model = Job
    template_name = 'companies/job/job-update.html'
    fields = ('title', 'job_level', 'employment_type', 'location', 'application_deadline','job_status')
    login_url = reverse_lazy('login')
    
    def test_func(self):
        Job = self.get_object()
        if self.request.user.company == Job.company:
            return True
        return False
    
    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('job-detail', kwargs={'pk': self.object.pk})
    
class CreateJob(LoginRequiredCompany, CreateView):
    model = Job
    template_name = 'companies/job/job-create.html'
    fields = ('title', 'job_level', 'employment_type', 'location', 'application_deadline','job_status')
    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('job-detail', kwargs={'pk': self.object.pk})
    
class DeleteJob(LoginRequiredCompany, UserPassesTestMixin, DeleteView):
    model = Job
    template_name = 'companies/job/job-delete.html'
    context_object_name = 'job'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('job-list')
    
    def test_func(self):
        Job = self.get_object()
        if self.request.user.company == Job.company:
            return True
        return False
    
    
    
    
class DetailJob(LoginRequiredCompany,DetailView):
    model = Job
    template_name = 'companies/job/job-detail.html'
    context_object_name = 'job'
    login_url = 'login'
    


# ------------------<> The Settings Side-bar <>------------------

#--------------------------------Branches------------------------------#
#----------------------------------------------------------------------#

class CompanyBranches(LoginRequiredCompany, ListView):
    model = Branch
    template_name = 'companies/settings/branches.html'
    context_object_name = 'branches'
    login_url = 'login'
    
    def get_queryset(self):
        # Ensure the user has an associated company to avoid potential errors
        if hasattr(self.request.user, 'company'):
            return Branch.objects.filter(company=self.request.user.company).order_by('-opened_on')
        return Branch.objects.none()

from django.db import transaction

class BranchCreateview(LoginRequiredCompany, CreateView):
    model = Branch
    fields = [ 'branch_image', 'name', 'location','branch_type', 'manager_name', 'phone_number','email', 'opened_on']
    template_name = 'companies/settings/branch_create.html'
    success_url = reverse_lazy('settings-branches')
    login_url = 'login'
        
    def form_valid(self, form):
        form.instance.company =  self.request.user.company
        return super().form_valid(form)

    


class BranchUpdate(LoginRequiredCompany, UserPassesTestMixin, UpdateView):
    model = Branch
    fields = [ 'branch_image', 'name', 'location','branch_type', 'manager_name', 'phone_number', 'opened_on']
    template_name = 'companies/settings/branch_update.html'
    success_url = reverse_lazy('settings-branches')
    login_url = 'login'

    def test_func(self):
        branch = self.get_object()
        if self.request.user.company == branch.company:
            return True
        return False
    
    def form_valid(self, form):
        form.instance.company =  self.request.user.company
        return super().form_valid(form)
    

    def form_invalid(self, form):
        return super().form_invalid(form)
    
class BranchDelete(LoginRequiredCompany, UserPassesTestMixin, DeleteView):
    model = Branch
    template_name = 'companies/settings/branch_delete.html'
    success_url = reverse_lazy('settings-branches')
    login_url = 'login'
    
    def test_func(self):
        branch = self.get_object()
        if self.request.user.company == branch.company:
            return True
        return False
    


#--------------------------------CompanyInfo------------------------------#
#----------------------------------------------------------------------#


class Companyinfo(LoginRequiredCompany, ListView):
    model = CompanyInfo
    template_name = 'companies/settings/company_info.html'
    context_object_name = 'info'
    login_url = 'login'
    
    def get_queryset(self):
        # Ensure the user has an associated company to avoid potential errors
        if hasattr(self.request.user, 'company'):
            return CompanyInfo.objects.get(company=self.request.user.company)
        return CompanyInfo.objects.none() 
    
    


class CompanyInfoUpdate(LoginRequiredCompany, UserPassesTestMixin, UpdateView):
    model = CompanyInfo
    fields = ['company_owner','industry', 'phone_number', 'established', 'revenue', 'founded_by', 'website', 'description']
    template_name = 'companies/settings/company_info_update.html'
    success_url = reverse_lazy('settings-company-info')
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        print(f"Received a {request.method} request at {request.path}")
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        companyin = self.get_object()
        if self.request.user.company == companyin.company:
            return True
        return False
    
    def form_valid(self, form):
        form.instance.company =  self.request.user.company
        if form.instance.company_owner:
            self.request.user.company.comp_info.company_owner = form.instance.company_owner
        return super().form_valid(form)
    

    
    

#--------------------------------Employee------------------------------#
#----------------------------------------------------------------------#

class CompanyEmployee(LoginRequiredCompany,ListView):
    model = Employee
    template_name = 'companies/settings/employee.html'
    context_object_name = 'employee'
    login_url = 'login'
    
    def get_queryset(self):
        # Ensure the user has an associated company to avoid potential errors
        if hasattr(self.request.user, 'company'):
            return Employee.objects.filter(company=self.request.user.company).order_by('first_name')
        return Employee.objects.none() 
    
class EmployeeCreate(LoginRequiredCompany, CreateView):
    model = Employee
    fields = ['employee_picture','first_name', 'last_name', 'email', 'phone', 'position']
    template_name = 'companies/settings/employee_create.html'
    success_url = reverse_lazy('settings-employee-info')
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)
    

    def form_invalid(self, form):
        return super().form_invalid(form)
    


class EmployeeUpdate(LoginRequiredCompany, UserPassesTestMixin, UpdateView):
    model = Employee
    fields = ['employee_picture','first_name', 'last_name', 'email', 'phone', 'position']
    template_name = 'companies/settings/employee_update.html'
    success_url = reverse_lazy('settings-employee-info')
    login_url = 'login'

    def test_func(self):
        Employee = self.get_object()
        if self.request.user.company == Employee.company:   
            return True
        return False
    
    def form_valid(self, form):
        form.instance.company =  self.request.user.company
        return super().form_valid(form)
    

    def form_invalid(self, form):
        return super().form_invalid(form)
    
class EmployeeDelete(LoginRequiredCompany, UserPassesTestMixin, DeleteView):
    model = Employee
    template_name = 'companies/settings/employee_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('settings-employee-info')
    login_url = 'login'
    
    def test_func(self):
        Employee = self.get_object()
        if self.request.user.company == Employee.company:
            return True
        return False




