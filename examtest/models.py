from django.db import models


# Create your models here.


class  SearchEngine(models.Model):

    keyword = models.CharField(max_length=20, null=False, blank=False) 
    user = models.CharField(max_length=20, null=False, blank=False)
    time = models.CharField(max_length=20, null=False, blank=False)
    location = models.TextField()
    device = models.TextField()
    created = models.DateTimeField(auto_now_add=True ,editable=False)
    modified = models.DateTimeField()

   
    

    def __str__(self):
        return self.keyword