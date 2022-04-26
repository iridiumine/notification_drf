from django.db import models


class User(models.Model):
    """
    用户管理
    """
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女'),
        (2, '未知'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=50)
    # organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)
    organization = models.CharField(max_length=50)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=2)
    mobile = models.CharField(max_length=11, unique=True)
    telephone = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=30, null=True)
    quote = models.TextField(null=True)
    avatar = models.CharField(max_length=255, null=True)
    # is_super = models.IntegerField(default=0)
    access = models.CharField(max_length=20, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User"
        db_table = "Users"
        ordering = ('created_time',)