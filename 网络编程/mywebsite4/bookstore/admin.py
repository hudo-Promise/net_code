from django.contrib import admin

# Register your models here.
from . import models


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']  # 是否链接到对象的更改页面
    list_filter =['pub']  # 是否添加到过滤器


admin.site.register(models.Book, BookManager)
admin.site.register(models.Author)
admin.site.register(models.Hero)
admin.site.register(models.Skill)