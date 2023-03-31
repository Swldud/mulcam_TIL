from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Article

# Create your views here.

def day_def(request):
    # render의 첫번째 인자 = request로 고정되어있음. 불변
    # 두번째 인자 = 템플릿 인자 'str'
    return render(request, 'day/day_def.html')





def new(request):
    return render(request, 'day/new.html')


def create(request):
    # 새로운 게시글(Article instance)을 생성

    article = Article()
    article.title = request.POST['title']
    article.time = request.POST['time']
    article.place = request.POST['place']
    article.memo = request.POST['memo']


    article.save()

    # return render(request, 'day/new.html')
    return redirect(f'/day/{article.pk}/')

def index(request):
    articles = Article.objects.all()

    return render(request, 'day/index.html', {'articles': articles,})
    # 얘는 변수 여러개, 리스트를 부르는 거니까 articles


# article_pk: var rounting으로 넘어온 값
# article_pk는 당연히 내가 urls에 작성한 변수명임. (변수= 이름을 언제든 내 마음대로 바꿀 수 있다. 단 짝을 잘 맞춰라!)
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    return render(request, 'day/detail.html', {'article': article})
    # 얘는 변수 딱 하나만 부르는 거니까 article



def delete(request, x):
    article = Article.objects.get(pk=x)
    article.delete()
    return redirect('/day/')


def edit(request, x):
    article = Article.objects.get(pk=x)
    return render(request, 'day/edit.html', {
        'article': article,
    })

def update(request, x):
    article = Article.objects.get(pk=x)
    article.title = request.POST['title']
    article.time = request.POST['time']
    article.place = request.POST['place']
    article.memo = request.POST['memo']
    article.save()
    return redirect(f'/day/{article.pk}/')