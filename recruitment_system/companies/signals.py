import logging
from companies.models import Company, Employee, Branch, CompanyInfo
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger(__name__)


# Set up logging
logger = logging.getLogger(__name__)

@receiver(pre_save, sender=Company, weak=True, dispatch_uid="Company_logo")
def set_default_company_logo(sender, instance, **kwargs):
    if instance.logo == "":
        instance.logo = 'company-logo.jpg'

@receiver(pre_save, sender=Branch, weak=True, dispatch_uid="Branch_image")
def set_default_branch_image(sender, instance, **kwargs):
    if instance.branch_image == "":
        instance.branch_image = 'branch-image.jpg'

@receiver(pre_save, sender=CompanyInfo, weak=True, dispatch_uid="Company_owner_image")
def set_default_company_owner_image(sender, instance, **kwargs):
    if instance.company_owner == "":
        instance.company_owner = 'company-owner.jpg'

@receiver(pre_save, sender=Employee, weak=True, dispatch_uid="Employee_image")
def set_default_employee_picture(sender, instance, **kwargs):
    if instance.employee_picture == "":
        instance.employee_picture = 'employee-image.jpg'


# --------------------------- Post Save Signal --------------------------------- #



@receiver(post_save, sender=Company, weak=True, dispatch_uid="Default_company_info_defining")
def create_company_info(sender, instance, created, **kwargs):
    if created:
        c_email=instance.c_user.email
        CompanyInfo.objects.create(company=instance,email=c_email)
        

@receiver(post_save, sender=Branch, dispatch_uid="Branch_number_upd")
def update_company_branch_count(sender, instance, created, **kwargs):
    company = instance.company  # Access the related company

    try:
        branch_no = company.c_branches.count()  # Count all branches related to the company
        # Get the CompanyInfo instance and update it
        company_info = CompanyInfo.objects.get(pk=company.comp_info.id)
        company_info.number_of_branches = branch_no

        # Update headquarters count only when a new Head Office is added
        if created and instance.branch_type == 'Head Office':
            company_info.headquarters = (company_info.headquarters or 0) + 1

        company_info.save()

    except ObjectDoesNotExist:
        logger.error(f"CompanyInfo for company {company.id} does not exist.")
    except Exception as e:
        logger.error(f"Unexpected error updating company branch count: {e}")
        
        

@receiver(post_delete, sender=Branch, weak=True, dispatch_uid="Branch_number_del")
def update_company_branch_count_on_delete(sender, instance, **kwargs):
    company = instance.company  # Access the related company
    
    try:
        branch_no = company.c_branches.count()  # Count all branches related to the company
        # Get the CompanyInfo instance and update it
        company_info = CompanyInfo.objects.get(pk=company.comp_info.id)
        company_info.number_of_branches = branch_no
        if instance.branch_type == 'Head Office' and company_info.headquarters > 0:
            company_info.headquarters -= 1 
        
        company_info.save()
    except ObjectDoesNotExist:
        # Log the error instead of printing
        logger.error(f"CompanyInfo for company {company.id} does not exist.")


@receiver(post_save, sender=Employee, weak=True, dispatch_uid="Employee_number_save")
def update_company_employee_count(sender, instance, created, **kwargs):
    company = instance.company  # Access the related company

    # Count all employees associated with the company
    employee_no = Employee.objects.filter(company=company).count()

    try:
        # Access the related CompanyInfo instance and update the employee count
        company_info = CompanyInfo.objects.get(pk=company.comp_info.id)
        company_info.employees = employee_no  # Set the employee count
        company_info.save()  # Save the updated employee count
    except ObjectDoesNotExist:
        # Log the error instead of printing
        logger.error(f"CompanyInfo for company {company.id} does not exist.")

@receiver(post_delete, sender=Employee, weak=True, dispatch_uid="Employee_number_del")
def update_company_employee_count_on_delete(sender, instance, **kwargs):
    company = instance.company  # Access the related company
    
    # Count all employees associated with the company
    employee_no = Employee.objects.filter(company=company).count()
    
    try:
        # Access the related CompanyInfo instance and update the employee count
        company_info = CompanyInfo.objects.get(pk=company.comp_info.id)
        company_info.employees = employee_no  # Set the employee count
        company_info.save()  # Save the updated employee count
    except ObjectDoesNotExist:
        # Log the error instead of printing
        logger.error(f"CompanyInfo for company {company.id} does not exist.")

        
      
       
       
#The line of code you provided uses the update_or_create() method of Django's QuerySet API to either update an existing record in the CompanyInfo model or create a new one if it doesn't exist. Here's a breakdown of the function of the company_info variable and the overall operation:

#Breakdown of update_or_create()
#Functionality:

#update_or_create() is a convenience method that attempts to retrieve an object matching the given parameters. If it finds an existing object, it updates it with the values specified in defaults. If it does not find a matching object, it creates a new one with the provided parameters.
#Parameters:

#company=company: This is the lookup field. The method checks if there is an existing CompanyInfo object with the specified company.
#defaults={'number_of_branches': branch_no}: This dictionary contains the fields to update or create. In this case, if the object exists, it updates the number_of_branches field with the value of branch_no. If it does not exist, it will create a new CompanyInfo object with the specified company and set its number_of_branches to branch_no.
#Return Value:

#The method returns a tuple consisting of:
#company_info: The instance of the CompanyInfo that was retrieved or created.
#created: A boolean that indicates whether a new object was created (True) or an existing object was updated (False).