from django.shortcuts import render
from django.http import HttpResponse

def image_a(request):
    # render의 첫번째 인자 = request로 고정
    # 두번째 인자 = 템플릿 인자 'str'
    return render(request, 'image_a.html')