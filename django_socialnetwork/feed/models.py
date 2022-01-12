from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.contrib.auth.models import User
from profiles.models import Profile






class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(
        upload_to='posts', 
        validators=[FileExtensionValidator(settings.ALLOWED_EXTENSIONS)],
        blank = True,
        null = True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    
    def __str__(self):
        return self.content[:20]
    
    def get_likes(self):
        return self.likes.all()
    
    def get_likes_count(self):
        return self.likes.all().count()
    
    def get_comments(self):
        return self.comments.all()
    
    def get_comment_count(self):
        return self.comments.all().count()
    
    class Meta:
        ordering = ('-created', )





class Comment(models.Model):
    content = models.TextField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content[:20]







