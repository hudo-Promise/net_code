from django.shortcuts import render


def test_form(request):
    if request.method == 'GET':
        return render(request, 'test_form.html')
    elif request.method == 'POST':
        pass


def show_meinv(request):
    return render(request, 'show_meinv.html')


def page1(request):
    return render(request, 'page1.html')