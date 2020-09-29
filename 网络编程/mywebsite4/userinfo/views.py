from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import models

# Create your views here.


def mylogin(request):
    if request.method == "GET":
        username = request.COOKIES.get('username', '')
        return render(request, 'login.html', locals())
    elif request.method == "POST":
        # 获取表单的数据
        remember = request.POST.get('remember', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # 验证用户名、密码是否正确
        try:
            user = models.User.objects.get(name=username,
                                           password=password)
            request.session['userinfo'] = {
                "username": user.name,
                'password': user.password
            }
        except:
            return HttpResponse('登陆失败')
        # 处理COOKIE
        resp = HttpResponse('登陆成功')
        if remember:
            resp.set_cookie('username', username, 7 * 24 * 60 * 60)
        else:
            resp.delete_cookie('username')
        return resp


def test_session(request):
    # 为session 添加mykey 对应的值
    request.session['mykey'] = ['北京', '上海']
    return HttpResponse('设置成功')


def show_session(request):
    value = request.session.get('mykey', 'mykey没有对应的值')
    s = str(value)
    return HttpResponse(s)


def myregister(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username', '')
        if username == '':
            username_error = "用户名不能为空"
            return render(request, 'register.html', locals())
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if password == '':
            password_error = "密码不能为空"
            return render(request, 'register.html', locals())
        elif password != password2:
            password2_error = "俩次密码不一样"
            return render(request, 'register.html', locals())
        else:
            # 注册功能
            try:
                user = models.User.objects.create(
                    name=username,
                    password=password,
                    role=1
                )
                return HttpResponse("注册成功")
            except:
                return HttpResponse('注册失败')


def mylogout(request):
    """退出登录"""
    if 'userinfo' in request.session:
        del request.session['userinfo']
    return HttpResponseRedirect('/')



