from django.urls import path
from .admin import job_admin

urlpatterns = [
    path('admin/', job_admin.urls),
]
