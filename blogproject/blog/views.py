from django.shortcuts import render
from blog.models import Article


def index(request):
    # return render(request, 'blog/index.html', context={
    #     'title': "Django博客",
    #     'welcome': "欢迎访问Django博客"
    # })
    article_list = Article.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'article_list': article_list})
