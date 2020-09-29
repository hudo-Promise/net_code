from django.http import HttpResponse


def page1(request):
    print("page被调用！")
    return HttpResponse("这是page1页")


def page2(request):
    html = '''
    <html>
    <head><title>这是页面2</title></head>
    <body>
    <h1>这是H1</h1>
    <h2 style="color:red;">这是H2 红色</h2>
    </body>
    </html>
        '''
    return HttpResponse(html)


def page3(request):
    html = '''
    显示自己想要的 内容
    '''
    return HttpResponse(html)


def page_year(request, y):
    html = "参数是：" + y
    return HttpResponse(html)


def birthday(request, y, m, d):
    html = "生日：" + y + "年" + m + "月" + d + "日"
    return HttpResponse(html)


def add(request, x, y):
    z = int(x) + int(y)
    html = "结果是：" + str(z)
    return HttpResponse(html)


def birth(request):
    if request.method == 'GET':
        year = request.GET.get("year", "0000")
        month = request.GET.get("month", "1")
        day = request.GET.get("day", "1")
        html = '生日是: ' + year + '年' + month + '月' + day + '日'
        return HttpResponse(html)


def search(request):
    html = '''
    <html>
    <head><title>搜索</title></head>
    <body>
    <form method='POST' action='/search/'>
    <input name='sss' type="text">
    <input type='submit'>
    </form>
    </body>
    </html>
        '''
    if request.method == 'GET':
        return HttpResponse(html)
    elif request.method == 'POST':
        sss = request.POST['sss']
        return HttpResponse('您正在POST提交 sss=' + sss)
    else:
        return HttpResponse("其他方式提交")