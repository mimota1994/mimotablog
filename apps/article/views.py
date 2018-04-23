#_*_encoding:utf-8_*_#
from django.shortcuts import render
from django.views.generic import View


from models import Article

from forms import ArticleForms

# Create your views here.


class ArticleDetailView(View):
    def get(self,request,article_id):
        article=Article.objects.get(id=article_id)

        #找到上下两篇文章
        try:
            left_article=Article.objects.filter(add_time__gt=article.add_time).order_by('-add_time')[0]
        except:
            left_article=[]

        try:
            right_article=Article.objects.filter(add_time__lt=article.add_time).order_by('-add_time')[0]
        except:
            right_article=[]

        url_address=request.get_full_path()

        content=article.content.encode('utf-8')

        if article:
            return render(request,'detail.html',{
                'article':article,
                'article_id_again':article_id,
                'left_article':left_article,
                'right_article':right_article,
                'url_address':url_address,
                'content':content
            })


class AddArticleView(View):
    def get(self,request):
        return render(request,'add_article.html')

    def post(self, request):
        article_forms = ArticleForms(request.POST)
        if article_forms.is_valid():
            article=Article()
            title = request.POST.get('title', '')
            content = request.POST.get('content', '')

            article.title=title
            article.content=content

            article.save()

            return render(request,'index.html')

