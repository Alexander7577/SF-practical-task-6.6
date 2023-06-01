from django.views.generic import ListView, DetailView
from .models import Post, Comment


class NewsList(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'news.html'
    context_object_name = 'news'


class PieceOfNewsDetail(DetailView):
    model = Post
    template_name = 'piece_of_news.html'
    context_object_name = 'piece_of_news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context['comments'] = post.comments.all()
        return context
