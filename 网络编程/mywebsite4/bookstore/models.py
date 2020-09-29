from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(verbose_name='书名', max_length=50, default='')
    pub = models.CharField(verbose_name='出版社', max_length=50, default='')
    price = models.IntegerField(verbose_name='价格', default=0)

    def __str__(self):
        return "书名：%s 出版社： %s" % (self.title, self.pub)


class Author(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=30, unique=True, db_index=True)
    age = models.IntegerField(verbose_name='年龄', default=1)
    email = models.EmailField(verbose_name='邮箱', default='', null=True)


class Skill(models.Model):
    name = models.CharField(verbose_name='技能', max_length=20, default='')
    level = models.IntegerField(verbose_name='伤害', default=1)


class Hero(models.Model):
    name = models.CharField(verbose_name='英雄', max_length=30)
    skill = models.OneToOneField(Skill, on_delete=models.CASCADE)

