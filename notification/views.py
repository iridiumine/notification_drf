from notification.models import Notification
from notification.serializers import NotificationSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class NotificationList(APIView):
    """
    List all notifications, or create a new notification.
    """

    def get(self, request,  *args, **kwargs):
        params = request.query_params
        filters = {k: v for k, v in params.items()}
        notifications = Notification.objects.filter(**filters)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationDetail(APIView):
    """
    Retrieve, update or delete a notification instance.
    """
    def get_object(self, pk):
        try:
            return Notification.objects.get(pk=pk)
        except Notification.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        notifications = self.get_object(pk)
        serializer = NotificationSerializer(notifications)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        notifications = self.get_object(pk)
        serializer = NotificationSerializer(notifications, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        notifications = self.get_object(pk)
        notifications.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)