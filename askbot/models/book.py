from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=120, blank=False, unique=True)
    notes = models.TextField(blank=True)
    class Meta:
        app_label = 'askbot'
                           
                            
class Book(models.Model):
    name = models.CharField(max_length=300, blank=False)
    edition = models.CharField(max_length=1000, blank=True)
    source_language = models.ForeignKey('Language')
    notes = models.TextField(blank=True)
    class Meta:
        unique_together = ('name', 'edition', 'source_language')
        app_label = 'askbot'
    

class Chapter(models.Model):
    book = models.ForeignKey('Book')
    num = models.IntegerField(blank=False)
    name = models.CharField(max_length=300, blank=True)
    notes = models.TextField(blank=True)
    class Meta:
        unique_together = ('book', 'num',)    
        app_label = 'askbot'
