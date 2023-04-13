from django.shortcuts import render, redirect
from .models import Article, Category, Comment, ReComment
from datetime import datetime, timezone

# Create your views here.
def new(request):
    if request.method == 'POST':

        print(request.POST)

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = Category.objects.get(name = request.POST['category']),
            deadline = request.POST['deadline'],
        )
        return redirect('home')

    return render(request, 'new.html')

def list(request, article_category):
    articles = Article.objects.filter(category = article_category)
    return render(request, 'list.html', {'articles': articles})

def detail(request, article_id):
    article = Article.objects.get(pk = article_id)

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            article = article,
            content = content
        )
        return redirect('detail', article_id)

    return render(request, 'detail.html', {'article': article})

def home(request):
    result = {
        'categories': []
    }

    categories = Category.objects.all()

    for category in categories:
        articles = Article.objects.filter(category = category)
        result['categories'].append([category, articles.count()])
        
    return render(request, 'home.html', result)

def todo(request):
    result = []
    d_day_list = []

    articles = Article.objects.filter(category_id = 4)
    
    for article in articles:
        d_date = article.deadline - datetime.now(timezone.utc)
        d_day = str(d_date).split(' ')[0]
        d_day = int(d_day)
        result.append([article, d_day])

    return render(request, 'todo.html', {'articles' : sorted(result, key=lambda x: x[1])})

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        Article.objects.filter(pk=article_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
        return redirect('detail', article_pk)
    
    return render(request, 'update.html', {'article': article})

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    
    return redirect('home')

def delete_comment(request, article_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('detail', article_id)

def base(request):
    return render(request, 'base.html)')

def recomment(request, article_id, comment_id):
    article = Article.objects.get(id=article_id)

    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        body = request.POST['content']
        ReComment.objects.create(
            comment = comment,
            body = body,
        )
        return redirect('detail', article_id)
    
    return render(request, 'detail.html', {'article' : article})

def delete_recomment(request, article_id, comment_id, recomment_id):
    recomment = ReComment.objects.get(id= recomment_id)
    recomment.delete()
    return redirect('detail', article_id)