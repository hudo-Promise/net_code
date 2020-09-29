from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField('用户名', max_length=30, unique=True)
    password = models.CharField('密码', max_length=30)
    role = models.IntegerField('角色', default=1)

    def __str__(self):
        return "用户" + self.name
