from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('blog/postcomment', views.postcomment, name="postcomment"),
    path('blog/', views.blog, name="blog"),
     
    path('blog/<str:slug>', views.blogpost, name="blogpost"),
    
    
    
    path('contact/', views.contact, name="contact"),
    path('search/', views.search, name="search"),
    path('signup', views.handleSignup, name="signup"),
    path('login', views.handleLogin, name="login"),
    path('logout', views.handleLogout, name="logout"),

]