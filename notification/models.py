from django.db import models
from user.models import User


class Notification(models.Model):
    """
    通知管理
    """
    STATE_CHOICES = (
        (0, 'unread'),
        (1, 'read'),
    )

    TYPE_CHOICES = (
        (0, 'diagnosis'),
        (1, 'manage'),
        (2, 'apply'),
    )

    LEVEL_CHOICES = (
        (0, 'normal'),
        (1, 'warning'),
        (2, 'fatal'),
    )

    id = models.AutoField(primary_key=True)
    target_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    state = models.IntegerField(choices=STATE_CHOICES, default=0)
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=0)
    content = models.TextField(null=True)
    post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Notificaitons"
        ordering = ('post_time',)