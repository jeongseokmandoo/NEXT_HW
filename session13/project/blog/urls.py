from django.urls import path, include
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name="home"),
    path('base', views.base, name='base'),
    path('new/', views.new, name="new"),
    path('detail/<int:post_pk>/', views.detail, name="detail"),
    path('update/<int:post_pk>/', views.update, name="update"),
    path('delete/<int:post_pk>/', views.delete, name="delete"),
    path("registration/signup/", views.signup, name="signup"),
    path("registration/login/", views.login, name="login"),
    path("registration/logout/", views.logout, name="logout"),
]