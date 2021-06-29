from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('welcome/', views.welcome, name="welcome"),
    url('^welcome/$', views.welcome, name="welcome")
]