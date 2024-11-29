from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

def validate_logo_size(logo):
    max_size_mb = 5
    allowed_extensions = {".jpg", ".jpeg", ".png"}
    
    # Check if file size exceeds the limit
    if logo.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Image size cannot exceed {max_size_mb} MB.")

class Company(models.Model):
    c_user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='company')
    logo = models.ImageField(upload_to="Companies/", validators=[validate_logo_size], verbose_name="Logo", blank=True,)
    name = models.CharField(max_length=255)  # Company name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  # Returns the company's name as its string representation


class CompanyInfo(models.Model):
    
    # ForeignKey to reference the Company model
    company_owner = models.ImageField(validators=[validate_logo_size],upload_to="Company_info/",blank=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE,related_name='comp_info')
    
    industry = models.CharField(max_length=50,null=True,blank=True)  # Industry the company belongs to
    established = models.DateField(default=timezone.now)  # Date when the company was established
    employees = models.SmallIntegerField(null=True, blank=True)  # Number of employees
    revenue = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)  # Annual revenue in USD
    headquarters = models.IntegerField(null=True,editable=False)  # Headquarters address
    founded_by = models.CharField(max_length=255, blank=True,null=True)  # Optional: Founder of the company
    number_of_branches = models.IntegerField(default=0, blank=True)  # Number of branches worldwide
    website = models.URLField(max_length=200, blank=True,null=True)  # Company's website (optional)
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=150,editable=False)
    description = models.TextField(max_length=500, blank=True,null=True)
    

    def __str__(self):
        return f"Additional Info for {self.company.name}"


class Branch(models.Model):
    BRANCH_TYPE_CHOICES = [
    ('Head Office', 'Head Office'),
    ('Branch Office', 'Branch Office'),
    ('Franchise', 'Franchise'),
    # Add more choices as necessary
    ]
    
    # ForeignKey to link branch to a company
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='c_branches')

    # Fields for the branch
    name = models.CharField(max_length=50)
    branch_type = models.CharField(max_length=30,choices=BRANCH_TYPE_CHOICES)
    manager_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(unique=True)
    location = models.CharField(max_length=50)
    email = models.EmailField(unique=True,max_length=100,blank=True, null=True)
    opened_on = models.DateField(default=timezone.now,editable=True)
    branch_image = models.ImageField(validators=[validate_logo_size],upload_to="Branches/", blank=True)

    def __str__(self):
        return f'{self.name} Managed {self.manager_name}'
    

class Employee(models.Model):
    # Company reference
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='c_employees')

    # Employee fields\
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,unique=True, blank=True,null=True)
    phone = PhoneNumberField(unique=True)
    country = CountryField(blank_label='(Select country)',default='RW')
    position = models.CharField(max_length=50,blank=True,null=True)
    employee_picture = models.ImageField(validators=[validate_logo_size],upload_to='Employees/', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.position}'
