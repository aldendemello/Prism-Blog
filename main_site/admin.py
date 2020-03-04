from django.contrib import admin
from .models import Post, Announce

admin.site.register(Post)
admin.site.register(Announce)

admin.site.site_header = "Game Name"
admin.site.site_title = "Game Name Portal"
admin.site.index_title = "Game Name"