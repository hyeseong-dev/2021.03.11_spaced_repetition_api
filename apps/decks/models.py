from django.db import models


class Deck(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_reviewed = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    

    # def total_cards():
        # return Deck.objects.filter(title=self.title)