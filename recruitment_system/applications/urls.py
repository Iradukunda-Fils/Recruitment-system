from django.urls import path
from applications.views import (
Home,Applications,Settings,NotificationView,Saved,UpdateApplication,ApplicationDelete
)


urlpatterns = [
    path('',Home.as_view(),name='application-home'),
    path('applications/',Applications.as_view(),name='applications'),
    path('saved-applications/',Saved.as_view(),name='saved-applications'),
    path('saved-application/application/<int:pk>',UpdateApplication.as_view(),name='saved-application-update'),
    path('saved-application/remove/<int:pk>',ApplicationDelete.as_view(),name='saved-application-delete'),
    path('notifications/',NotificationView.as_view(),name='notification'),
    path('profile-settings/',Settings.as_view(),name='profile-settings'),
]