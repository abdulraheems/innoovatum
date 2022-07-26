import datetime
from haystack import indexes
from .models import Website

class WebsiteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #title = indexes.CharField(model_attr='title', faceted=True)
    link = indexes.CharField(model_attr='link', faceted=True)

    title = indexes.EdgeNgramField(model_attr='title')

                             
    def get_model(self):
        return Website
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()