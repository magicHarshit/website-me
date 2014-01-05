from django.db import models


class ContactDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    messages = models.TextField()

    def __unicode__(self):
        return self.name