"""
URL configuration for JSM_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from JSM_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.base, name='base'),
    path('', views.home, name='home'),
    path('new', views.new, name='new'),
    path('list/<str:article_category>', views.list, name='list'),
    path('detail/<int:article_id>', views.detail, name='detail'),
    path('todo', views.todo, name='todo'),
    path('update/<int:article_pk>/', views.update, name="update"),
    path('delete/<int:article_pk>/', views.delete, name="delete"),
    path('delete-comment/<int:article_id>/<int:comment_id>', views.delete_comment, name='delete-comment'),
    path('recomment/<int:article_id>/<int:comment_id>', views.recomment, name='recomment'),
    path('delete-recomment/<int:article_id>/<int:comment_id>/<int:recomment_id>', views.delete_recomment, name='delete-recomment'),
]
