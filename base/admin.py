from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
from .models import Tag,Post
class PostAdmin(admin.ModelAdmin):

    formfield_overrides={
        models.TextField:{'widget': TinyMCE() }
        }

admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
