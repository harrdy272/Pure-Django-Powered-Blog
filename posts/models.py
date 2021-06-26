from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    label = models.CharField(max_length=100, default="General-Awareness")
    upload = models.ImageField(upload_to = "media", default="logo.jpg")
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def datepublished(self):
        return self.date_published.strftime('%B %d, %Y')

