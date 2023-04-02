from django.urls import path

from . import views

app_name = 'day'


urlpatterns = [
    # 생성을 위한 코드

    # day/create/
    path('create/', views.create, name='create'),
    
    
    # 조회를 위한 코드
    # day/   # index는 메인페이지로 이어진다는 느낌이 있음
    path('', views.index, name='index'),
    
    # day/숫자
    path('<int:article_pk>/', views.detail, name='detail'),
    
    # Delete

    # day/숫자/delete/
    path('<int:article_pk>/delete/', views.delete, name = 'delete'),
    # x는 숫자 변수임.

    # Update

    # blog/1/update/
    path('<int:article_pk>/edit/', views.edit, name = 'edit'),



]