from django.contrib import admin
from . models import Contact, Post , BlogComment
# Register your models here.

admin.site.register(Contact)
admin.site.register(( BlogComment))


@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)
 
