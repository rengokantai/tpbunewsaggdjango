__author__ = 'Hernan Y.Ke'
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$',views.articles_list,name='articles_list')
]