from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Blog, Entry
from .forms import BlogForm, EntryForm

def index(request):
    """Home page for our blogs app."""
    return render(request, 'blogs/index.html')

def check_blog_owner(blog, request):
    """Check the blog's owner."""
    if blog.owner != request.user:
        raise Http404

@login_required
def blogs(request):
    """Show blog list."""
    blogs = Blog.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

@login_required
def blog(request, blog_id):
    """Show individual blog page."""
    blog = get_object_or_404(id=blog_id)
    check_blog_owner(blog, request)

    entries = blog.entry_set.order_by('date_added')
    context = {'blog': blog, 'entries': entries}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    """Start a new blog."""
    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogs')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_entry(request, blog_id):
    """Add a new entry for a particular blog."""
    blog = get_object_or_404(id=blog_id)
    check_blog_owner(blog, request)

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.blog = blog
            new_entry.save()
            return redirect('blogs:blog', blog_id=blog_id)

    # Display a blank or invalid form.
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = get_object_or_404(id=entry_id)
    blog = entry.blog
    check_blog_owner(blog, request)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id = blog.id)

    context = {'entry': entry, 'blog': blog, 'form':form}
    return render(request, 'blogs/edit_entry.html', context)