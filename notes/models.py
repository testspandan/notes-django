from django.db import models

class Note(models.Model):
    content = models.TextField()
    class Meta:
        app_label = 'notes'
    def __str__(self):
        return self.content
