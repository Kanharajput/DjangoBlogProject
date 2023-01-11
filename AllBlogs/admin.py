from django.contrib import admin
from .models import Post,Author,Tag,Comment

# register this class as well with Post model then you will see the difference
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}         # this will pre fill the slug field by checking title field
    list_display = ("title","date","author",)             # show entries with this three columns value
    list_filter = ("date","author",)                         # let us filter with this two columns

class CommentAdmin(admin.ModelAdmin):
    list_display  = ("user_name","post",)      # show username and post to represent comments in admin panel

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment,CommentAdmin)