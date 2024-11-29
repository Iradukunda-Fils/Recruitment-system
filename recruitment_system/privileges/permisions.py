from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import AnonymousUser

#------------------- Company ----------------

class LoginAuth(LoginRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        # First check if the user is authenticated
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        
        user_role = request.user.role

        # Check if the user is an instance of AnonymousUser (this is redundant if we already check is_authenticated)
        if isinstance(request.user, AnonymousUser):
            raise PermissionDenied("You do not have permission to access this page.")

        # Check if the user has a 'company' attribute or a role
        if not hasattr(request.user, 'role'):
            raise PermissionDenied("You must be associated with a company to access this page.")
        return super().dispatch(request, *args, **kwargs)
    

class LoginRequiredCompany(LoginRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        # First check if the user is authenticated
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        
        user_role = request.user.role

        # Check if the user is an instance of AnonymousUser (this is redundant if we already check is_authenticated)
        if isinstance(request.user, AnonymousUser):
            return super().dispatch(request, *args, **kwargs)
            

        # Check if the user has a 'company' attribute or a role
        if not getattr(request.user, 'company', None) or not hasattr(request.user, 'role'):
            raise PermissionDenied("You must be associated with a company to access this page.")

        # Check if the user has the correct role
        if user_role != 'company':
            raise PermissionDenied("You must have the 'company' role to access this page.")
        
        return super().dispatch(request, *args, **kwargs)

#-------------------- User --------------------

class LoginRequiredUser(LoginRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        user_role = request.user.role
        
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        elif user_role != 'applicant':
                raise PermissionDenied("You do not have permission to access this page.")
        
        return super().dispatch(request, *args, **kwargs)


# Check if the user has a 'company' attribute (indicating association with a company)
#        if not getattr(request.user, 'company', None):
#           # Redirect to the company registration page if the user is not associated with a company
#           return redirect(reverse('company-registration'))