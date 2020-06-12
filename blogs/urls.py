"""URL patterns for blogs app."""

from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Blogs list page.
    path('blogs/', views.blogs, name='blogs'),
    # Individual blog page.
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    # Page for adding a new blog topic.
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page for adding a new entry for a given blog
    path('new_entry/<int:blog_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry for a given blog
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]