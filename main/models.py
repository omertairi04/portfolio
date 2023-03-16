from django.db import models

from django.contrib.auth.models import User

SKILL_LEVELS = (
    ('Beginner' , 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Confident' , 'Confident'),
    ('Professional', 'Professional')
)

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    age = models.IntegerField(default=18)
    profilepic = models.ImageField(upload_to='profilepics')
    short_intro = models.CharField(max_length=500)
    bio = models.TextField()
    skills = models.ManyToManyField('Skills',blank=True)
    CV = models.FileField(blank=True , null=True)
    resume = models.FileField(blank=True , null=True)
    github = models.CharField(max_length=555)
    linkedin = models.CharField(max_length=555)
    instagram = models.CharField(max_length=555)
    twitter = models.CharField(max_length=555)
    facebook = models.CharField(max_length=555)

    def __str__(self):
        return str(self.name)

class Skills(models.Model):
    name = models.CharField(max_length=255)
    skill_level = models.CharField(max_length=255 ,choices=SKILL_LEVELS)
    description = models.TextField(blank=True , null=True)

    def __str__(self):
        return str(self.name)

class Projects(models.Model):
    author = models.ForeignKey(Profile , on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    github = models.CharField(max_length=555 , blank=True , null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    content_image = models.ManyToManyField('Image' ,blank=True)
    skills = models.ManyToManyField(Skills,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)
    
class BlogPosts(models.Model):
    author = models.ForeignKey(Profile , on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='blog-thumbnails/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Image(models.Model):
    content_image = models.ImageField(upload_to='content/')
    text = models.CharField(max_length=255,  blank=True , null=True)

    def __str__(self):
        return str(f'{self.text}')



