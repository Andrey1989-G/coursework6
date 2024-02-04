from django.views.generic import ListView, DetailView

from blogs.models import Blog
from blogs.forms import BlogForm


class BlogListView(ListView):
    model = Blog
    form_class = BlogForm

class BlogDetailView(DetailView):
    model = Blog
    form_class = BlogForm