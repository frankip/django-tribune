from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =200)
    last_name = models.CharField(max_length =200)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

class Tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE,)
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


        