from django.contrib import admin
from .models import Blog, Entry

# username = 'blog_admin'
# password = 'blog_admin_password'

admin.site.register(Blog)
admin.site.register(Entry)