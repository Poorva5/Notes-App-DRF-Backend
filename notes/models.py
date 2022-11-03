from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title