from django.urls import path
from .views import WebHomeView,JobListView,DetailJob

urlpatterns = [
    path('',WebHomeView.as_view(),name='home'),
    path('job-list/', JobListView.as_view(),name='home-job-list'),
    path('job-list/detail/<int:pk>', DetailJob.as_view(), name='home-job-detail'),
]