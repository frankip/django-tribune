from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('welcome/', views.welcome, name="welcome"),
    url('^articles/$', views.welcome, name="welcome"),
    path('about/', views.about, name="about"),
    path('about/<str:name>', views.about_name, name="about-name"),
    path('article/<int:article_id>', views.single_article, name="single-article"),
    # url('^about/(\name)/$', views.about_name, name="about"),
]