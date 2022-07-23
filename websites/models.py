from email.mime import image
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse



class Website(models.Model):
    title = models.CharField(max_length=255)
    link = models.TextField()
    content = models.TextField()
    logo = models.ImageField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}:{}..".format(self.id, self.link)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title

