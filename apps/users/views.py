#_*_encoding:utf-8_*_#
from django.shortcuts import render
from django.views.generic import View

from article.models import Article
from pure_pagination import Paginator,PageNotAnInteger

import requests


# Create your views here.

class IndexView(View):
    def get(self,request):
        all_articles=Article.objects.all().order_by('-add_time')

        #分页功能
        try:
            page=request.GET.get('page',1)
        except PageNotAnInteger:
            page=1

        p=Paginator(all_articles,3,request=request)

        article=p.page(page)




        #诗歌api，用requests模块读取
        url='http://miaoxiaoer.com/api/getpoem.miao'
        respose=requests.request("GET",url).content
        return render(request,'index.html',{
            "all_articles":article,
            'poet':respose

        })


class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')