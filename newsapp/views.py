from django.shortcuts import render
#models
from .models import Article
# Create your views here.

def welcome(request):
    articles = Article.retrieve_articles()
    # date= datetime.date()
    ctx = {
        "articles": articles,
    }
    return render(request, 'articles.html', ctx)

def about(request):

    return render(request, 'about.html')

def about_name(request, name):
    ctx = {
        "name" : name
        }
    print('name',name )
    return render(request, 'about1.html', ctx)

def single_article(request, article_id):
    try:
        single_article = Article.retrieve_single_article(article_id)

    except DoesNotExist:
        raise Http404()

    ctx = {
        "single_article": single_article
    }
    return render(request, 'single-article.html', ctx)
