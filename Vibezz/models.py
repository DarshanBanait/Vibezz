from django.db import models
from django.utils import timezone

class PoemGeneration(models.Model):
    theme = models.CharField(max_length=100)
    mood = models.CharField(max_length=50)
    recipient = models.CharField(max_length=100)
    prompt = models.TextField()
    generated_poem = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Poem about {self.theme} ({self.mood}) - {self.created_at.strftime('%Y-%m-%d %H:%M')}"