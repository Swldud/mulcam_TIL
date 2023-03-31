from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# redirect는 응답으로 화면을 보여주는게 아니라, ~ 이라고 보내! 라고 지시 -> 다시 요청 -> 응답 (render와 비교하기 위해서는 url을 확인할 것)

from .models import Article
# 여기서 Article은 day라는 앱 안에서 만든 model의 이름
# -> app의 admin에 등록해주었음 (출생신고 마냥 등록)
# 태어난 Article이라는 이름의 모델이 출생신고까지 했으니까 이제 사용가능 허가를 받은거나 마찬가지
# -> views.py 파일에서 함수를 만들 때 필요하다면 얼마든지 사용 가능해졌다. (= 로또할 때 random이라는 모듈을 사용했던 것처럼 새로운 모듈로서 활용이 가능하다.) 
# 단, from .models import Article 으로 나 얘 사용할게! 하고 언급을 해줘야 함

# Create your views here.

def new(request):
    return render(request, 'day/new.html')


def create(request):
    # 새로운 게시글(Article instance)을 생성

    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
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
