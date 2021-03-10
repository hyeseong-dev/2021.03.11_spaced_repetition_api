from django.db import models
from apps.utils.models import TimeStamps

class Deck(TimeStamps):
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_reviewed = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    

    # def total_cards():
        # return Deck.objects.filter(title=self.title)