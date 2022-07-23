import datetime
from django.utils import timezone
from haystack import indexes
from .models import Blog

class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #title = indexes.CharField(model_attr='title', faceted=True, boost=1.125)
    detail = indexes.CharField(model_attr='detail', faceted=True)

    #title = indexes.EdgeNgramField(model_attr='title',use_template=True,boost=1.125)
    
    # for auto complete
    title = indexes.EdgeNgramField(model_attr='title',boost=1.125)

    # Spelling suggestions
    suggestions = indexes.FacetCharField()
                             
    def get_model(self):
        return Blog
    
    def index_queryset(self, using=None):
        #return self.get_model().objects.all()
        return self.get_model().objects.filter(created_at__lte=timezone.now())