from django.urls import path
from .views import RegistrationView,AuthLoginView,LogoutView

urlpatterns = [
    path('logout/',LogoutView.as_view(),name='logout'),
    path('login/',AuthLoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('registration/',RegistrationView.as_view(),name='register'),
]