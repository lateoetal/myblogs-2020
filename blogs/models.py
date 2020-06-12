from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """A blog title model."""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

class Entry(models.Model):
    """A blog entry that users are going to write."""
    blog  = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            self.text = self.text[:50]
            return f"{self.text}..."
        else:
            return self.text
