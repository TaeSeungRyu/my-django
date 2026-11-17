from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

#python manage.py makemigrations board
#python manage.py migrate        