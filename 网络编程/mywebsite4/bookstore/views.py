from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.db.models import F, Q
from django.http import Http404

# Create your views here.


def add_book(request):
    if request.method == 'GET':
        title = request.GET.get('title',)
        publish = request.GET.get('pub')
        models.Book.objects.create(title=title, pub=publish)
        return HttpResponse('ok')


def index(request):
    return render(request, 'index.html')


def new_book(request):
    if 'userinfo' not in request.session:
        raise Http404
    if request.method == 'GET':
        return render(request, 'new_book.html')
    elif request.method == 'POST':
        t = request.POST.get('title', '')
        pub = request.POST.get('pub', '')
        price = request.POST.get('price', 0)
        m_price = request.POST.get('market_price', 0)
        # 方法一
        # abook = models.Book.objects.create(title=t,
        #                                    pub=pub,
        #                                    price=price,
        #                                    market_price=m_price)
        abook = models.Book()
        abook.title = t
        abook.pub = pub
        abook.save()  # 保存并提交
        return HttpResponse('添加成功')


def list_book(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html', locals())


def filter_book(request):
    books = models.Book.objects.filter(pub='清华大学出版社')
    return render(request, 'book_list.html', locals())


def test_f(request, up):
    """up代表涨价的幅度"""
    books = models.Book.objects.all()
    # for book in books:
    #     p = float(book.price)
    #     p += up
    #     book.price = p
    #     book.save()
    books.update(price=F('price') - float(up))
    return HttpResponse("整体价格调整完成")


def test_q(request):
    book = models.Book.objects.filter(Q(price__lt=20) | Q(pub='清华大学出版社'))


def one2one(request):
    skill_one = models.Skill.objects.create(
        name='如来神掌', level=20
    )
    hero = models.Hero.objects.create(
        name='盲僧', skill=skill_one
    )
    skill_two = models.Skill.objects.create(
        name='狂风绝息斩', level=20
    )
    hero = models.Hero.objects.create(
        name='亚索', skill=skill_two
    )
    return HttpResponse('添加成功')