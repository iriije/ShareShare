from django.contrib import admin
from .models import Post,Sharer,ItemType,Items

admin.site.register(Post)
admin.site.register(Sharer)
admin.site.register(ItemType)
admin.site.register(Items)
