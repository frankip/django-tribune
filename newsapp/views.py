from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#models
from .models import Article
from .forms import NewArticleForm 
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

@login_required(login_url='/accounts/login/')
def single_article(request, article_id):
    try:
        single_article = Article.retrieve_single_article(article_id)

    except DoesNotExist:
        raise Http404()

    ctx = {
        "single_article": single_article
    }
    return render(request, 'single-article.html', ctx)

def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('welcome')
    else:
        form = NewArticleForm()
    return render(request, 'new-article.html', {'form':form})