from django.shortcuts import render,redirect
from .models import Article,Feed
from .forms import FeedForm
import datetime
import feedparser

# Create your views here.
def articles_list(request):
    articles = Article.objects.all()
    return render(request,'news/articles_list.html',{'articles':articles})

def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request,'news/feeds_list.html',{'feeds':feeds})

def new_feed(request):
    if request.method=="POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feedData = feedparser.parse(feed.url)
            feed.title = feedData.feed.title
            feed.save()
            for entry in feedData.entries:
                article = Article()
                article.title = entry.title
                article.url =entry.link
                article.description = entry.description
                d = datetime.detetime(*(entry.published_parsed[0:6]))
                dateString = d.strftime('%Y-%m-%d %H:%M:%S')
                article.publication_date = dateString
                article.feed = feed
                article.save()
            return redirect('news.views.feeds_list')
    else:
        form = FeedForm()
    return render(request,'news/new_feed.html',{'form':form})