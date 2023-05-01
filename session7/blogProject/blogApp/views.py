from django.shortcuts import render, redirect
from .models import Article, Category

# Create your views here.
def new(request):
    if request.method == 'POST':

        print(request.POST)

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = Category.objects.get(name = request.POST['category'])
        )
        return redirect('category')

    return render(request, 'new.html')

def list(request, article_category):
    articles = Article.objects.filter(category = article_category)
    return render(request, 'list.html', {'articles': articles})

def detail(request, article_id):
    article = Article.objects.get(pk = article_id)
    return render(request, 'detail.html', {'article': article})

def category(request):
    result = {
        'categories': []
    }

    categories = Category.objects.all()

    for category in categories:
        articles = Article.objects.filter(category = category)
        result['categories'].append([category, articles.count()])
        
    return render(request, 'category.html', result)