from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Commit(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.PositiveIntegerField()
    article = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.full_name
