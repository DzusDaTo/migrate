from django.shortcuts import render


def test1(request):
    return render(request, 'main/html/test.html')
