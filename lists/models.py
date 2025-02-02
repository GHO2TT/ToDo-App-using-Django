from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class twoDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('complete',)


def __str__(self):
    return self.title