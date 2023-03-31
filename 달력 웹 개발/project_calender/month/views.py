from django.shortcuts import render
from django.http import HttpResponse



def month_main(request):

    return render(request, 'month/month_main.html')