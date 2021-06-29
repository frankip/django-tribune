from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('welcome/', views.welcome, name="welcome"),
    url('^welcome/$', views.welcome, name="welcome"),
    path('about/', views.about, name="about"),
    path('about/<name>', views.about_name, name="about"),
    # url('^about/(\name)/$', views.about_name, name="about"),
]