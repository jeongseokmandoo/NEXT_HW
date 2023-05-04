from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect(request.GET.get('next', '/blog/'))
        error = "아이디 또는 비밀번호가 틀립니다"
        return render(request, 'blog/registration/login.html', {"error" : error})
    
    return render(request, 'blog/registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('blog:home')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        exist_user = User.objects.filter(username=username)

        if exist_user:
            error = "이미 존재하는 유저입니다."
            return render(request, 'blog/registration/signup.html', {"error" : error})
        
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        return redirect('blog:home')
    
    return render(request, 'blog/registration/signup.html')

def base(request):
    return render(request, 'blog/base.html)')

def home(request):
    posts = Post.objects.all()

    return render(request, 'blog/home.html', {'posts' : posts})

@login_required(login_url="/blog/registration/login/")
def new (request):
    if request.method== "POST":
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('blog:detail', new_post.pk)
    
    return render(request, 'blog/new.html')

@login_required(login_url="/blog/registration/login/")
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    return render(request, 'blog/detail.html', {'post' : post})

@login_required(login_url="/blog/registration/login/")
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('blog:detail', post_pk)
    
    return render(request, 'blog/update.html', {'post': post})

@login_required(login_url="/blog/registration/login/")   
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('blog:home')