from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from .models import Article
from .forms import ArticleForm


# Create your views here.

# def new(request):
#     return render(request, 'day/new.html')


# def create(request):
#     # 새로운 게시글(Article instance)을 생성

#     article = Article()
#     article.title = request.POST['title']
#     article.time = request.POST['time']
#     article.place = request.POST['place']
#     article.memo = request.POST['memo']


#     article.save()

#     # return render(request, 'day/new.html')
#     return redirect('day:detail', article.pk)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'GET':
        form = ArticleForm()

    else:
        form = ArticleForm(request.POST)
        if form.is_valid:
            article = form.save()
            return redirect('day:detail', article.pk)
        
    return render(request, 'day/create.html', {'form': form})


@require_safe
def index(request):
    articles = Article.objects.all()

    return render(request, 'day/index.html', {'articles': articles,})
    # 얘는 변수 여러개, 리스트를 부르는 거니까 articles


# article_pk: var rounting으로 넘어온 값
# article_pk는 당연히 내가 urls에 작성한 변수명임. (변수= 이름을 언제든 내 마음대로 바꿀 수 있다. 단 짝을 잘 맞춰라!)

@require_safe
def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk = article_pk)

    return render(request, 'day/detail.html', {'article': article})
    # 얘는 변수 딱 하나만 부르는 거니까 article


@require_safe
def delete(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk = article_pk)
    article.delete()
    return redirect('day:index')
    


# def edit(request, x):
#     article = Article.objects.get(pk=x)
#     return render(request, 'day/edit.html', {
#         'article': article,
#     })

# def update(request, x):
#     article = Article.objects.get(pk=x)
#     article.title = request.POST['title']
#     article.time = request.POST['time']
#     article.place = request.POST['place']
#     article.memo = request.POST['memo']
#     article.save()
#     return redirect('day:detail', article.pk)


@require_http_methods(['GET', 'POST'])
def edit(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk = article_pk)

    if request.method == 'GET':
        form = ArticleForm(instance=article)
        
    elif request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()

            return redirect('day:detail', article.pk)

    return render(request, 'day/edit.html', {
        'form': form,
    })
