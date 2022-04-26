from user.models import User
from user.serializers import UserSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from notification.models import Notification
from notification.serializers import NotificationSerializer


# Create your views here.


class UserListView(APIView):
    """
    filter the users
    """
    def get(self, request, format=None):
        params = request.query_params
        filters = {k: v for k, v in params.items() if k != 'current' and k != 'pageSize' }
        users = User.objects.filter(**filters)
        ser_users = UserSerializer(users, many=True)
        return Response(ser_users.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    get: view user detail
    put: update user detail
    """
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        if user:
            ser_user = UserSerializer(user)
            return Response(ser_user.data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': '用户信息未找到'}, status=status.HTTP_404_NOT_FOUND)


    def put(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        if user:
            ser_user = UserSerializer(user, request.data, partial=True)
            if ser_user.is_valid():
                ser_user.save()
                return Response({'msg': '用户信息更新成功'}, status=status.HTTP_200_OK)
            else:
                return Response(ser_user.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg': '用户信息未找到'}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        access = str(user.access)
        if user and access.find('0') < 0:
            # 删除和更新团队消息
            teams_member = user.team_member_created_user.all()
            for team_member in teams_member:
                team = team_member.team
                team.count = team.count - 1
                team.save()
            user.delete()
            print(teams_member)
            return Response({'msg': '删除用户成功'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': '删除用户失败'}, status=status.HTTP_404_NOT_FOUND)


class UserNotificationDetail(APIView):
    """
    get: view user's notifications detail
    """
    def get(self, request,  *args, **kwargs):
        pk = self.kwargs['pk']
        notifications = Notification.objects.filter(target_user=pk).all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
