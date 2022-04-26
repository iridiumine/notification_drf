from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('<int:pk>', views.UserDetail.as_view()),
    path('<int:pk>/notifications', views.UserNotificationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)