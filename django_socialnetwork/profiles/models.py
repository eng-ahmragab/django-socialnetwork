from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .utils import get_random_code





# Note:
# fields with default values are not required, So we can keep Blank and Null False to prevent users from clearing them




class Profile(models.Model):
    # blank = True, makes the field optional in the forms
    name = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(default = "no bio...", blank=True, null=True)
    #image is not blank or null, so we don't allow users to remove the default image
    avatar = models.ImageField(upload_to='profile-pics', default='profile-pics/avatar.png')
    created = models.DateTimeField(auto_now_add=True) #can't be set by user
    updated = models.DateTimeField(auto_now=True) #can't be set by user
    slug = models.SlugField(unique=True, blank=True)    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # related_name is how the other table access this one
    followers = models.ManyToManyField(User, blank=True, related_name='following')
    
    
    def __str__(self):
        return f"<Profile({self.user.username}, {self.created.strftime('%d.%m.%Y %H:%M:%S')})>"
    
    def get_posts(self):
        return self.user.posts.all()
    
    def get_posts_count(self):
        return self.user.posts.all().count()
    
    def get_followers(self):
        return self.followers.all()
    
    def get_followers_count(self):
        return self.followers.all().count()
    
    def get_following(self):
        return Profile.objects.filter(followers__in = [self.user])
    
    def get_following_count(self):
        profiles_following = Profile.objects.filter(followers__in = [self.user])
        return len(profiles_following)
    
    
    def generate_slug(self):
        if self.name:
            # to get a slug of the name
            slug = slugify(str(self.name))
            slug_exists = Profile.objects.filter(slug=slug).exists()
            # add random code is they exist
            while slug_exists:
                slug = slugify(slug + ' ' + get_random_code())
                slug_exists = Profile.objects.filter(slug=slug).exists()
        else:
            slug = str(self.user)
        return slug
    
    # overriding the object save method
    def save(self, *args, **kwargs):
        # set slug of the current instance
        if not self.slug:
            self.slug = self.generate_slug()
        # call the parent's save()
        super().save()






