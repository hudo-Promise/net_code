from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# 方式 一
def page1_template(request):
    t = loader.get_template("page1.html")
    html = t.render()
    return HttpResponse(html)
    # return render(request, "xxx.html")


class Dog:
    def __init__(self, kind, color):
        self.kind =  kind
        self.color = color

    def info(self):
        return self.color + "的" + self.kind + "狗"


# 方式 二
def page2_render(request):
    t = loader.get_template("page2.html")
    dict = {"name": '张三', "age": '18', 'favorite': ['看书', '看电影'],
            "friend": {'name': '小张', 'age': '25'}, 'pet': Dog('二哈', '黑白相间')}
    html = t.render(dict)
    return HttpResponse(html)
    # return render(request, 'page2.html', dict)
