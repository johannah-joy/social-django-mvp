from django.shortcuts import render
# from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from posts.models import Post
from users.forms import PostForm

# Create your views here.

# def addTweet(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST or None) 
#         if form.is_valid(): 
#             form.save()
#             posts = Post.objects.all()
#             return render(request, 'my-tweets.html', {'posts': posts})
#     else:
#         form_class = PostForm
#     return render(request, "add-tweet.html", {
#         'form': form_class,})

class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'add-tweet.html'
    fields = ['text','author']
    exclude = ('author') 

    def form_vaild(self, form): 
        form.instance.author=self.request.user
        return super().form_valid(form)



# def myTweets(request):
#     text_input = request.POST.get('text')
#     date_published_input = request.POST.get('date_published')
#     author_input = request.POST.get('author')
#     Post.objects.create(text=text_input, date_published=date_published_input, author=author_input)
#     items = Post.objects.all()
#     context = {'content': items}
#     return render(request, 'my-tweets.html', context)

class TweetListView(generic.ListView):
    model = Post
    template_name = 'home.html'
    # context_object_name = 'posts'
    # ordering = ['-date_published']