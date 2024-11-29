from django.urls import path
from .admin import company_admin
from .views import (
    Home, ManageUsers, Analytics, Settings,
    
    # ----------------------<> jobs Views <>--------------------#
    JobList,DetailJob,UpdateJob,DeleteJob,CreateJob,
    
    # --------------------<> settings Views <>------------------#
    CompanyBranches, BranchCreateview, BranchUpdate, BranchDelete,
    #-----------------------------------------------------------#
    Companyinfo, CompanyInfoUpdate,
    #-----------------------------------------------------------#
    CompanyEmployee, EmployeeCreate, EmployeeUpdate, EmployeeDelete,

)

urlpatterns = [
    path('admin/',company_admin.urls),
    path('',Home.as_view(),name='company-home'),
    path('user_management',ManageUsers.as_view(),name='manage-users'),
    path('analytics', Analytics.as_view(), name='analytic'),
    
#-----------------------------------------------<> Job URL <>------------------------------------#
#---------------------------------------------<> <> <> <> <> <>----------------------------------#
    path('jobs/', JobList.as_view(), name='job-list'),
    path('jobs/create/', CreateJob.as_view(), name='job-create'),
    path('jobs/Detail/<int:pk>', DetailJob.as_view(), name='job-detail'),
    path('jobs/update/<int:pk>', UpdateJob.as_view(), name='job-update'),
    path('jobs/delete/<int:pk>', DeleteJob.as_view(), name='job-delete'),
    

#--------------------------------------------<> Settings URL <>----------------------------------#
#---------------------------------------------<> <> <> <> <> <>----------------------------------#
    path('settings/', Settings.as_view(), name='settings'),
    
#----------------------------------<> Branches URL <>--------------------------------------------#
    path('settings/blanches/', CompanyBranches.as_view(), name='settings-branches'),
    path('settings/blanche-create/', BranchCreateview.as_view(), name='settings-branches-create'),
    path('settings/blanche-update/<int:pk>/', BranchUpdate.as_view(), name='settings-branches-update'),
    path('settings/blanche-delete/<int:pk>/', BranchDelete.as_view(), name='settings-branches-delete'),
    
#---------------------------------<> Company Info URL <>-----------------------------------------#
    path('settings/company-info/', Companyinfo.as_view(), name='settings-company-info'),
    path('settings/company-info-update/<int:pk>/', CompanyInfoUpdate.as_view(), name='settings-company-info-update'),
    
#---------------------------------<> Employee Info URL <>-----------------------------------------#
    path('settings/employee-info/', CompanyEmployee.as_view(), name='settings-employee-info'),
    path('settings/employee-create/', EmployeeCreate.as_view(), name='settings-employee-create'),
    path('settings/employee-info-update/<int:pk>/', EmployeeUpdate.as_view(), name='settings-employee-update'),
    path('settings/employee-delete/<int:pk>/', EmployeeDelete.as_view(), name='settings-employee-delete'),
    
    
]