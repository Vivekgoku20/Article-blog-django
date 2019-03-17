from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True, blank=True)
    thumb=models.ImageField(default='dafault.png',blank=True)
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE) 

# python3 manage.py makemigrations
# python3 manage.py migrate

    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]+"..."