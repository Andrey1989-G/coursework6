from django.urls import path
from django.views.decorators.cache import cache_page

from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogDetailView

app_name = BlogsConfig.name

urlpatterns = [
    path('blog/', cache_page(60)(BlogListView.as_view()), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_view'),
]