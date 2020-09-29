from django.db import models
from django.utils import timezone     # required for adding timestamp info
from uuid import uuid4  # required for custom id using UUIDs

# Create your models here.
class Note(models.Model):

    NOTES_KINDS = (
        ('random', 'RANDOM'),
        ('important', 'IMPORTANT'),
        ('misc', 'MISC'),
    )

    id = models.UUIDField( primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 100)
    content = models.TextField(blank = True) # allowed to be blank
    time_stamp = models.DateTimeField(default = timezone.now)
    kinds = models.CharField(max_length=50, choices = NOTES_KINDS, default = 'misc')

    def __str__(self):
        return self.title