from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserCreationForm
from privileges.permisions import LoginAuth
from django.views import View

# Create your views here.

class LogoutView(LoginAuth, View):
    login_url = reverse_lazy('login')
    success_url  = reverse_lazy('login')
    tempelate_name = 'logout.html'
    
    def get(self, request):
        return render(request,self.tempelate_name)
    
    def post(self, request):
        logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect(self.success_url)


class AuthLoginView(LoginView):
    template_name = 'authentication/login.html'

    def get_success_url(self):
        if self.request.user.role == 'company':
            return reverse_lazy('company-home')
        elif self.request.user.role == 'applicant':
            return reverse_lazy('application-home')
        else:
            # Add error message and redirect to a safe fallback URL
            messages.error(self.request, 'Permission denied.')
            return reverse_lazy('home')
    
    
class RegistrationView(CreateView):
    form_class = UserCreationForm  # Reference the form class, not an instance
    template_name = 'authentication/registration.html'
    success_url = reverse_lazy('login')
    
    
    
    
    
    
    
    
    
    
#     from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.contrib.auth import update_session_auth_hash
# from django.contrib import messages
# from django import forms
# from django.contrib.auth.models import User

# # Custom form to handle username, email, and role
# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'is_staff']

# @login_required
# def update_user_credentials(request):
#     user = request.user
#     password_form = PasswordChangeForm(user)
#     user_form = UserUpdateForm(instance=user)

#     if request.method == "POST":
#         password_form = PasswordChangeForm(user, request.POST)
#         user_form = UserUpdateForm(request.POST, instance=user)

#         if password_form.is_valid() and user_form.is_valid():
#             # Save the new password
#             password_form.save()
#             # Save updated user information
#             user_form.save()
#             # Keep the user logged in after password change
#             update_session_auth_hash(request, password_form.user)
#             messages.success(request, "Your credentials have been updated successfully!")
#             return redirect('profile')  # Redirect to a profile page or desired URL
#         else:
#             messages.error(request, "Please correct the errors below.")

#     return render(request, 'update_credentials.html', {
#         'password_form': password_form,
#         'user_form': user_form
#     })
