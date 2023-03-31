
from django.urls import path
from . import views


urlpatterns = [

    # 생성을 위한 코드
    
    # day/new/
    path('new/', views.new, name='new'),
    # day/create/ [사용자 입력 데이터]
    path('create/', views.create, name='create'),
    
    
    # 조회를 위한 코드
    # day/   # index는 메인페이지로 이어진다는 느낌이 있음
    path('', views.index, name='index'),
    
    # day/숫자
    path('<int:article_pk>/', views.detail, name='detail'),
    
    # Delete

    # day/숫자/delete/
    path('<int:x>/delete/', views.delete, name = 'delete')
    # x는 숫자 변수임.
    
]
