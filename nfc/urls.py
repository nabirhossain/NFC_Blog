from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy, re_path
from . import views

app_name = 'nfc'

urlpatterns = [
    path('',views.index,name='index'),
    path('author/<name>',views.getAuthor,name='author'),
    path('detail/<int:id>',views.PostDetail, name='post_detail'),
    path('category/<name>',views.PostTopic, name='category'),
    path('login',views.LogIn, name='login'),
    path('logout',views.LogOut, name='logout'),
    path('create',views.CreatePost, name='create'),
    path('profile',views.profile, name='profile'),
    path('update/<int:id>',views.PostUpdate, name='update'),
    path('delete/<int:id>',views.PostDelete, name='delete'),
    path('register',views.register, name='register'),
    path('topics',views.ShowTopic, name='category'),
    path('create/topic',views.AddCategory, name='createTopic'),
    path('pdf/<int:id>',views.pdf.as_view(), name='pdf'),
    path('about/',views.About, name='about'),
    path('activity/',views.PortFolio, name='activity'),
    #passward management

    #account confirmation url
    path('activate/<uid>/<token>',views.activate, name='activate'),

]