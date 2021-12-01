from django.urls import path

from . import views

urlpatterns = [
    path('myclasses/', views.myClasses),
    path('getschedule/', views.getSchedule),
    path('addclass/', views.addClass),
    path('myclasses/<class_code>', views.class_info),
    path('locations/', views.location_list),
    path('notifications/', views.notifications),
    path('addnotification/', views.addNotification),
    path('delete/event/<event_id>/', views.deleteEvent),
    path('delete/class/<class_id>/', views.deleteClass)
]