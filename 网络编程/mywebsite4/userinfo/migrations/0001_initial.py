# Generated by Django 3.0.5 on 2020-09-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
                ('role', models.IntegerField(default=1, verbose_name='角色')),
            ],
        ),
    ]
