# Project : project_scheduler

## App name : month

## project_scheduler - month

- month/main
    - 사용자에게 달력을 제공
    - 토요일은 파란색
    - 일요일 및 공휴일은 빨간색

## project_scheduler - day

- day/날짜(숫자)/new/
    - 사용자에게 글을 작성하는 HTML을 제공
    - new.html

- day/날짜(숫자)/create/
    - 사용자가 POST로 보낸 데이터를 저장
    - 상세 페이지로 redirect

- day/날짜(숫자)/
    - 전체 게시글(article)을 조회하는 HTML을 제공
    - 게시글은 제목만 표시하며, 링크로 구성한다
    - index.html

- day/날짜(숫자)/게시글번호
    - 특정 게시글을 조회하는 HTML을 제공
    - 게시글의 제목/내용/작성시간/수정시간을 보여준다.
    - detail.html