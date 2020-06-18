from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('home/', views.TweetListView.as_view(), name='home'),
    # path('home/', views.home, name='home'),
    path('add-tweet/', views.TweetCreateView.as_view(), name='add-tweet'),
    # path('add-tweet/', views.addTweet, name='add-tweet'),
    # path('my-tweets/', views.TweetListView.as_view(), name='my-tweets'),
    # path('my-tweets/', views.myTweets, name='my-tweets'),
]