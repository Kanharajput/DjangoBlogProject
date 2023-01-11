from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

# Tag model having tags for posts
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    # represent tag objects by caption 
    def __str__(self):
        return self.caption


# Author model having relation one to many with Post model
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_addr = models.EmailField()

    # represent Author object by their name
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# having post data 
class Post(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)    # put the date in the field at which time we are saving the data
    image = models.ImageField(upload_to="Images", null=True)          # upload images to Images folder which will be inside MEDIA_ROOT
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])    # TextFields same like CharField
    slug = models.SlugField(unique=True, db_index=True)     # set it as unique because we are going to use it as a primary key
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name='posts',null=True)      # one to many relation 
    tags = models.ManyToManyField(Tag)              # ManyToManyRelation with tag

    # represent post entry by it post title
    def __str__(self):
        return self.title
    

# comment to store user comment 
class Comment(models.Model):
    user_name = models.CharField(max_length=30)
    email_addr = models.EmailField()
    text = models.TextField(max_length=100)
    # I think here we use cross model queries to find comments of a post from that post model
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")