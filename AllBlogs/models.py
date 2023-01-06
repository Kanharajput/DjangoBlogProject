from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

# Tag model having tags for posts
class Tag(models.Model):
    caption = models.CharField(max_length=20)


# Author model having relation one to many with Post model
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_addr = models.EmailField()

# having post data 
class Post(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)    # put the date in the field at which time we are saving the data
    image_name = models.CharField(max_length=50)          # later on we upload files right now we get images from static folder
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])    # TextFields same like CharField
    slug = models.SlugField(unique=True, db_index=True)     # set it as unique because we are going to use it as a primary key
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name='posts',null=True)      # one to many relation 
    tags = models.ManyToManyField(Tag)              # ManyToManyRelation with tag

