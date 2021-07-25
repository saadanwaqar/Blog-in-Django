from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=30)
    desc = models.CharField(max_length=3000)

    def __str__(self) :
        return self.name


class Post(models.Model):
     
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=300)
    # views = models.IntegerField(default=0) 
    desc = models.TextField() 
    timestamp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=33)

    def __str__(self) : 
        return self.title + ' by ' + self.author



class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True )
    comment = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True) 
    timestamp = models.DateTimeField(default=now)  

    def __str__(self) :
        return self.comment[0:13]+ "... " + " by " +  self.user.username