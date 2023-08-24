from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request) : 
    articles = Article.objects.all()

    context = {
        'articles' : articles
    }

    return render(request, 'index.html', context) 

def create(request) : 
    if request.method == 'POST':
        form = ArticleForm(request,POST)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
        
    else:
        form = ArticleForm()

    context = {
            'form' : form,
    }

    return render(request, 'create.html', context)
