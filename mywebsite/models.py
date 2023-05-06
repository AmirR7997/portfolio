from django.db import models

from block import settings


class Project (models.Model):
    title = models.CharField(max_length=100)
    decsription = models.CharField(max_length=250)
    image = models.FileField(upload_to = 'mywebsite/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name= 'post_categories', null = True, blank = True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post likes')

    def __str__(self):
        return self.title + ' | ' + str(self.author
                                        )