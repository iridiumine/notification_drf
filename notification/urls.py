from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from notification import views

urlpatterns = [
    path('notifications/', views.NotificationList.as_view()),
    path('notifications/<int:pk>/', views.NotificationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)